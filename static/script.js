document.addEventListener('DOMContentLoaded', function() {
    // --- Elements ---
    const chatMessages = document.getElementById('chatMessages');
    const userInput = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');
    const sidebarToggleBtn = document.getElementById('sidebarToggleBtn');
    const sidebarCloseBtn = document.getElementById('sidebarCloseBtn');
    const appSidebar = document.getElementById('appSidebar');
    const charCounter = document.getElementById('charCounter');
    
    // Controls Elements
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const soundToggle = document.getElementById('soundToggle');
    const soundIcon = document.getElementById('soundIcon');
    const exportBtn = document.getElementById('exportBtn');
    const clearBtn = document.getElementById('clearBtn');
    
    // Search elements
    const topicSearch = document.getElementById('topicSearch');
    const searchResultsList = document.getElementById('searchResultsList');

    // --- State Variables ---
    let soundEnabled = localStorage.getItem('sound_enabled') !== 'false'; // default true
    let isSending = false;

    // List of all indexed questions for client-side sidebar search
    const INDEXED_QUESTIONS = [
        "What are the requirements for Computer Science?",
        "Can I apply with my qualifications?",
        "Do you offer Nursing?",
        "What courses are available in the Faculty of Science?",
        "How do I apply?",
        "What documents do I need?",
        "When does admission close?",
        "How much is the tuition?",
        "What are the acceptance fees?",
        "Where is the campus location?",
        "What faculties and departments do you have?",
        "Where is the admissions office?",
        "How can I contact the university?",
        "What are the office hours?",
        "When does the semester start?",
        "When are exams?",
        "When does course registration end?",
        "What happens if I miss course registration?",
        "Can I change my course?",
        "How do I apply for accommodation?",
        "How much is the hostel fee?",
        "Can I defer my admission?",
        "When is the exam timetable released?",
        "When are results released?",
        "How much is the tuition for Computer Science?",
        "What other fees/charges are there?",
        "What are the payment procedures?",
        "What are the payment deadlines and options?",
        "What is the attendance policy?",
        "What are the examination rules?",
        "What is the dress code?",
        "What are the graduation requirements?",
        "What is the university code of conduct?",
        "I need help with a problem / office contacts",
        "What is the escalation process?"
    ];

    // --- Sound Synthesis (Web Audio API) ---
    // Zero dependencies, synthesized directly in the browser!
    let audioCtx = null;
    
    function initAudio() {
        if (!audioCtx) {
            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
    }

    function playSound(type) {
        if (!soundEnabled) return;
        try {
            initAudio();
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
            
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            
            const now = audioCtx.currentTime;
            
            if (type === 'send') {
                // Soft click/pluck sound
                osc.type = 'sine';
                osc.frequency.setValueAtTime(600, now);
                osc.frequency.exponentialRampToValueAtTime(150, now + 0.08);
                
                gain.gain.setValueAtTime(0.15, now);
                gain.gain.linearRampToValueAtTime(0.001, now + 0.08);
                
                osc.start(now);
                osc.stop(now + 0.08);
            } else if (type === 'receive') {
                // Pleasant double chime: C5 (523Hz) then E5 (659Hz)
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(523.25, now); // C5
                osc.frequency.setValueAtTime(659.25, now + 0.08); // E5
                
                gain.gain.setValueAtTime(0.0, now);
                gain.gain.linearRampToValueAtTime(0.12, now + 0.02);
                gain.gain.setValueAtTime(0.12, now + 0.08);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
                
                osc.start(now);
                osc.stop(now + 0.35);
            }
        } catch (e) {
            console.warn('Audio synthesis failed:', e);
        }
    }

    // --- Core Functions ---

    // Public method registered to window for quick suggestion buttons
    window.quickQuestion = function(question) {
        userInput.value = question;
        userInput.dispatchEvent(new Event('input')); // Update character counter
        sendMessage();
        
        // Auto-close sidebar on mobile after clicking
        if (window.innerWidth <= 992) {
            appSidebar.classList.remove('open');
        }
    };

    function addMessage(messageText, isUser, followUps = []) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.innerHTML = messageText;
        
        messageDiv.appendChild(contentDiv);
        chatMessages.appendChild(messageDiv);
        
        // Render follow-up chips if present
        if (!isUser && followUps && followUps.length > 0) {
            const chipsContainer = document.createElement('div');
            chipsContainer.className = 'follow-up-container';
            
            followUps.forEach(qText => {
                const btn = document.createElement('button');
                btn.className = 'follow-up-btn';
                btn.textContent = qText;
                btn.addEventListener('click', () => {
                    window.quickQuestion(qText);
                });
                chipsContainer.appendChild(btn);
            });
            
            chatMessages.appendChild(chipsContainer);
        }
        
        // Auto scroll to bottom & render icons
        setTimeout(() => {
            const container = document.querySelector('.chat-messages-container');
            container.scrollTop = container.scrollHeight;
            if (window.lucide) {
                lucide.createIcons();
            }
        }, 50);
    }

    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot';
        typingDiv.id = 'typingIndicator';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.innerHTML = `
            <div class="typing-dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
        `;
        
        typingDiv.appendChild(contentDiv);
        chatMessages.appendChild(typingDiv);
        
        const container = document.querySelector('.chat-messages-container');
        container.scrollTop = container.scrollHeight;
    }

    function removeTypingIndicator() {
        const indicator = document.getElementById('typingIndicator');
        if (indicator) {
            indicator.remove();
        }
    }

    async function sendMessage() {
        const message = userInput.value.trim();
        if (message === '' || isSending) return;
        
        isSending = true;
        userInput.value = '';
        userInput.disabled = true;
        sendBtn.disabled = true;
        charCounter.textContent = '0/150';
        
        // Render user message bubble
        addMessage(message, true);
        playSound('send');
        showTypingIndicator();
        
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            // Add a slight delay to the response to make it feel natural
            setTimeout(() => {
                removeTypingIndicator();
                addMessage(data.response, false, data.follow_ups);
                playSound('receive');
                
                userInput.disabled = false;
                sendBtn.disabled = false;
                userInput.focus();
                isSending = false;
            }, 600);
            
        } catch (error) {
            console.error('Error:', error);
            removeTypingIndicator();
            addMessage('Sorry, there was an error connecting to the server. Please try again.', false);
            
            userInput.disabled = false;
            sendBtn.disabled = false;
            isSending = false;
        }
    }

    // --- Sidebar Client-Side Search ---
    topicSearch.addEventListener('input', function() {
        const query = this.value.toLowerCase().trim();
        searchResultsList.innerHTML = '';
        
        if (query === '') {
            searchResultsList.style.display = 'none';
            return;
        }
        
        const matches = INDEXED_QUESTIONS.filter(q => q.toLowerCase().includes(query)).slice(0, 5);
        
        if (matches.length > 0) {
            searchResultsList.style.display = 'flex';
            matches.forEach(match => {
                const btn = document.createElement('button');
                btn.className = 'search-result-item';
                btn.textContent = match;
                btn.title = match;
                btn.addEventListener('click', () => {
                    window.quickQuestion(match);
                    topicSearch.value = '';
                    searchResultsList.innerHTML = '';
                    searchResultsList.style.display = 'none';
                });
                searchResultsList.appendChild(btn);
            });
        } else {
            searchResultsList.style.display = 'none';
        }
    });

    // --- Controls and Settings ---

    // Initialize Sound Status UI
    function updateSoundUI() {
        const iconName = soundEnabled ? 'volume-2' : 'volume-x';
        const text = soundEnabled ? 'Sound: On' : 'Sound: Off';
        
        const newIcon = document.createElement('i');
        newIcon.id = 'soundIcon';
        newIcon.setAttribute('data-lucide', iconName);
        
        const oldIcon = document.getElementById('soundIcon');
        if (oldIcon) {
            oldIcon.replaceWith(newIcon);
        }
        soundToggle.querySelector('.btn-text').textContent = text;
        
        if (soundEnabled) {
            soundToggle.classList.remove('secondary-btn');
        } else {
            soundToggle.classList.add('secondary-btn');
        }
        localStorage.setItem('sound_enabled', soundEnabled);
        if (window.lucide) {
            lucide.createIcons();
        }
    }
    
    soundToggle.addEventListener('click', () => {
        soundEnabled = !soundEnabled;
        updateSoundUI();
        if (soundEnabled) {
            playSound('receive');
        }
    });
    updateSoundUI();

    // Theme Toggle Helper Function
    function updateThemeUI(isDark) {
        const iconName = isDark ? 'sun' : 'moon';
        const text = isDark ? 'Light Theme' : 'Dark Theme';
        
        const newIcon = document.createElement('i');
        newIcon.id = 'themeIcon';
        newIcon.setAttribute('data-lucide', iconName);
        
        const oldIcon = document.getElementById('themeIcon');
        if (oldIcon) {
            oldIcon.replaceWith(newIcon);
        }
        themeToggle.querySelector('.btn-text').textContent = text;
        
        if (window.lucide) {
            lucide.createIcons();
        }
    }

    // Theme Toggle Handler
    const savedTheme = localStorage.getItem('theme') || 'dark';
    if (savedTheme === 'light') {
        document.body.classList.remove('dark-theme');
        document.body.classList.add('light-theme');
        updateThemeUI(false);
    } else {
        document.body.classList.remove('light-theme');
        document.body.classList.add('dark-theme');
        updateThemeUI(true);
    }

    themeToggle.addEventListener('click', () => {
        if (document.body.classList.contains('dark-theme')) {
            document.body.classList.remove('dark-theme');
            document.body.classList.add('light-theme');
            updateThemeUI(false);
            localStorage.setItem('theme', 'light');
        } else {
            document.body.classList.remove('light-theme');
            document.body.classList.add('dark-theme');
            updateThemeUI(true);
            localStorage.setItem('theme', 'dark');
        }
    });

    // Clear Conversation Handler
    clearBtn.addEventListener('click', () => {
        if (confirm('Are you sure you want to clear the conversation history?')) {
            chatMessages.innerHTML = `
                <div class="message bot">
                    <div class="message-content">
                        Welcome to the <b>University Enquiry Portal</b>! 👋<br><br>
                        I am your smart assistant, powered by natural language processing. Ask me any question in plain English, and I will search our official documentation to give you a direct, precise answer.<br><br>
                        <b>To get started, select a category below or type your question:</b>
                    </div>
                </div>
            `;
            playSound('send');
            if (window.lucide) {
                lucide.createIcons();
            }
        }
    });

    // Export Chat History Handler
    exportBtn.addEventListener('click', () => {
        let historyText = `==================================================\n`;
        historyText += `UNIVERSITY ENQUIRY PORTAL CHAT HISTORY\n`;
        historyText += `Export Date: ${new Date().toLocaleString()}\n`;
        historyText += `==================================================\n\n`;
        
        const messages = chatMessages.querySelectorAll('.message');
        if (messages.length <= 1) {
            alert('No chat history to export.');
            return;
        }

        messages.forEach(msg => {
            const isUser = msg.classList.contains('user');
            const sender = isUser ? 'STUDENT' : 'ASSISTANT';
            const content = msg.querySelector('.message-content').innerText;
            historyText += `[${sender}]:\n${content}\n\n`;
        });
        
        const blob = new Blob([historyText], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `university_chat_history_${Date.now()}.txt`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    });

    // --- Mobile Layout Helpers ---
    sidebarToggleBtn.addEventListener('click', () => {
        appSidebar.classList.add('open');
    });

    sidebarCloseBtn.addEventListener('click', () => {
        appSidebar.classList.remove('open');
    });

    // Close sidebar on tapping outside on mobile
    document.addEventListener('click', (e) => {
        if (window.innerWidth <= 992) {
            if (!appSidebar.contains(e.target) && !sidebarToggleBtn.contains(e.target) && appSidebar.classList.contains('open')) {
                appSidebar.classList.remove('open');
            }
        }
    });

    // Character Counter
    userInput.addEventListener('input', function() {
        const len = this.value.length;
        charCounter.textContent = `${len}/150`;
        if (len >= 140) {
            charCounter.style.color = 'var(--primary-red)';
        } else {
            charCounter.style.color = 'var(--text-muted)';
        }
    });

    // --- Event Listeners for Input ---
    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Auto-focus input on launch
    userInput.focus();

    // Initialize Lucide Icons
    if (window.lucide) {
        lucide.createIcons();
    }
});