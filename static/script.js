document.addEventListener('DOMContentLoaded', function () {

    // ── DOM Elements ──────────────────────────────────────────────────────────
    const chatMessages    = document.getElementById('chatMessages');
    const chatContainer   = document.getElementById('chatContainer');
    const userInput       = document.getElementById('userInput');
    const sendBtn         = document.getElementById('sendBtn');
    const charCounter     = document.getElementById('charCounter');

    const appSidebar        = document.getElementById('appSidebar');
    const sidebarOverlay    = document.getElementById('sidebarOverlay');
    const sidebarToggleBtn  = document.getElementById('sidebarToggleBtn');
    const sidebarCloseBtn   = document.getElementById('sidebarCloseBtn');

    const themeToggle = document.getElementById('themeToggle');
    const soundToggle = document.getElementById('soundToggle');
    const exportBtn   = document.getElementById('exportBtn');
    const clearBtn    = document.getElementById('clearBtn');

    const topicSearch       = document.getElementById('topicSearch');
    const searchResultsList = document.getElementById('searchResultsList');

    // ── State ─────────────────────────────────────────────────────────────────
    let soundEnabled = localStorage.getItem('sound_enabled') !== 'false';
    let isSending = false;

    // ── Indexed Questions (for sidebar search) ────────────────────────────────
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
        "What is the escalation process?",
        "Are there any scholarships?",
        "What is the SIWES / internship program?",
        "What are the student health services?",
        "How do I replace a lost ID card?",
        "What are the requirements for MBA / postgraduate admission?",
        "I can't log in to the student portal",
        "How do I access campus WiFi?",
        "What student clubs and associations are available?",
        "Is there a study abroad or exchange program?",
        "How do I request an official transcript?",
        "How do I collect my certificate?",
        "What is the supplementary / retake exam policy?",
        "What is the CGPA grading scale?",
        "What is the academic probation or suspension policy?"
    ];

    // ── Web Audio Synthesis ───────────────────────────────────────────────────
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
            if (audioCtx.state === 'suspended') audioCtx.resume();
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            const now = audioCtx.currentTime;
            if (type === 'send') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(600, now);
                osc.frequency.exponentialRampToValueAtTime(150, now + 0.08);
                gain.gain.setValueAtTime(0.15, now);
                gain.gain.linearRampToValueAtTime(0.001, now + 0.08);
                osc.start(now); osc.stop(now + 0.08);
            } else if (type === 'receive') {
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(523.25, now);
                osc.frequency.setValueAtTime(659.25, now + 0.08);
                gain.gain.setValueAtTime(0, now);
                gain.gain.linearRampToValueAtTime(0.12, now + 0.02);
                gain.gain.setValueAtTime(0.12, now + 0.08);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
                osc.start(now); osc.stop(now + 0.35);
            }
        } catch (e) { console.warn('Audio error:', e); }
    }

    // ── Sidebar Helpers ───────────────────────────────────────────────────────
    function openSidebar() {
        appSidebar.classList.add('open');
        sidebarOverlay.classList.add('visible');
        sidebarOverlay.removeAttribute('aria-hidden');
        document.body.style.overflow = 'hidden'; // prevent bg scroll on mobile
    }

    function closeSidebar() {
        appSidebar.classList.remove('open');
        sidebarOverlay.classList.remove('visible');
        sidebarOverlay.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    }

    sidebarToggleBtn.addEventListener('click', openSidebar);
    sidebarCloseBtn.addEventListener('click', closeSidebar);
    sidebarOverlay.addEventListener('click', closeSidebar);

    // Close sidebar on desktop resize
    window.addEventListener('resize', () => {
        if (window.innerWidth >= 1024) closeSidebar();
    });

    // ── Core Functions ────────────────────────────────────────────────────────
    window.quickQuestion = function (question) {
        userInput.value = question;
        userInput.dispatchEvent(new Event('input'));
        closeSidebar();
        sendMessage();
    };

    function scrollToBottom() {
        requestAnimationFrame(() => {
            chatContainer.scrollTop = chatContainer.scrollHeight;
            if (window.lucide) lucide.createIcons();
        });
    }

    function addMessage(text, isUser, followUps = []) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${isUser ? 'user' : 'bot'}`;
        const content = document.createElement('div');
        content.className = 'message-content';
        content.innerHTML = text;
        msgDiv.appendChild(content);
        chatMessages.appendChild(msgDiv);

        if (!isUser && followUps && followUps.length > 0) {
            const chipsWrap = document.createElement('div');
            chipsWrap.className = 'follow-up-container';
            followUps.forEach(q => {
                const btn = document.createElement('button');
                btn.className = 'follow-up-btn';
                btn.textContent = q;
                btn.addEventListener('click', () => window.quickQuestion(q));
                chipsWrap.appendChild(btn);
            });
            chatMessages.appendChild(chipsWrap);
        }

        scrollToBottom();
    }

    function showTyping() {
        const el = document.createElement('div');
        el.className = 'message bot';
        el.id = 'typingIndicator';
        el.innerHTML = `<div class="message-content"><div class="typing-dots"><span></span><span></span><span></span></div></div>`;
        chatMessages.appendChild(el);
        scrollToBottom();
    }

    function removeTyping() {
        const el = document.getElementById('typingIndicator');
        if (el) el.remove();
    }

    async function sendMessage() {
        const msg = userInput.value.trim();
        if (!msg || isSending) return;

        isSending = true;
        userInput.value = '';
        userInput.disabled = true;
        sendBtn.disabled = true;
        charCounter.textContent = '0/200';

        addMessage(msg, true);
        playSound('send');
        showTyping();

        try {
            const res = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: msg })
            });
            const data = await res.json();

            setTimeout(() => {
                removeTyping();
                addMessage(data.response, false, data.follow_ups);
                playSound('receive');
                userInput.disabled = false;
                sendBtn.disabled = false;
                userInput.focus();
                isSending = false;
            }, 550);

        } catch (err) {
            console.error('Chat error:', err);
            removeTyping();
            addMessage('Sorry, there was a connection error. Please try again.', false);
            userInput.disabled = false;
            sendBtn.disabled = false;
            isSending = false;
        }
    }

    // ── Sidebar Search ────────────────────────────────────────────────────────
    topicSearch.addEventListener('input', function () {
        const q = this.value.toLowerCase().trim();
        searchResultsList.innerHTML = '';
        if (!q) { searchResultsList.style.display = 'none'; return; }

        const hits = INDEXED_QUESTIONS.filter(item => item.toLowerCase().includes(q)).slice(0, 6);
        if (hits.length) {
            searchResultsList.style.display = 'flex';
            hits.forEach(h => {
                const btn = document.createElement('button');
                btn.className = 'search-result-item';
                btn.textContent = h;
                btn.title = h;
                btn.setAttribute('role', 'option');
                btn.addEventListener('click', () => {
                    window.quickQuestion(h);
                    topicSearch.value = '';
                    searchResultsList.style.display = 'none';
                });
                searchResultsList.appendChild(btn);
            });
        } else {
            searchResultsList.style.display = 'none';
        }
    });

    // ── Sound Toggle ──────────────────────────────────────────────────────────
    function updateSoundUI() {
        const icon = soundEnabled ? 'volume-2' : 'volume-x';
        const text = soundEnabled ? 'Sound: On' : 'Sound: Off';
        const newEl = document.createElement('i');
        newEl.id = 'soundIcon';
        newEl.setAttribute('data-lucide', icon);
        const old = document.getElementById('soundIcon');
        if (old) old.replaceWith(newEl);
        soundToggle.querySelector('.btn-text').textContent = text;
        soundEnabled
            ? soundToggle.classList.remove('secondary-btn')
            : soundToggle.classList.add('secondary-btn');
        localStorage.setItem('sound_enabled', soundEnabled);
        if (window.lucide) lucide.createIcons();
    }

    soundToggle.addEventListener('click', () => {
        soundEnabled = !soundEnabled;
        updateSoundUI();
        if (soundEnabled) playSound('receive');
    });
    updateSoundUI();

    // ── Theme Toggle ──────────────────────────────────────────────────────────
    function applyTheme(dark) {
        document.body.classList.toggle('dark-theme', dark);
        document.body.classList.toggle('light-theme', !dark);
        const iconName = dark ? 'sun' : 'moon';
        const newEl = document.createElement('i');
        newEl.id = 'themeIcon';
        newEl.setAttribute('data-lucide', iconName);
        const old = document.getElementById('themeIcon');
        if (old) old.replaceWith(newEl);
        themeToggle.querySelector('.btn-text').textContent = dark ? 'Light Mode' : 'Dark Mode';
        localStorage.setItem('theme', dark ? 'dark' : 'light');
        if (window.lucide) lucide.createIcons();
    }

    const savedTheme = localStorage.getItem('theme') || 'dark';
    applyTheme(savedTheme === 'dark');

    themeToggle.addEventListener('click', () => {
        applyTheme(document.body.classList.contains('light-theme'));
    });

    // ── Clear Chat ────────────────────────────────────────────────────────────
    clearBtn.addEventListener('click', () => {
        if (!confirm('Clear this conversation?')) return;
        chatMessages.innerHTML = `
            <div class="message bot">
                <div class="message-content">
                    Welcome to the <b>University Enquiry Portal</b>! 👋<br><br>
                    I'm your smart assistant powered by natural language processing. Ask me anything — I'll search the knowledge base and give you a direct answer.<br><br>
                    <b>Try:</b> <i>"How do I apply?"</i>, <i>"How much is tuition for nursing?"</i>, <i>"When does school resume?"</i>
                </div>
            </div>`;
        playSound('send');
        if (window.lucide) lucide.createIcons();
    });

    // ── Export Chat ───────────────────────────────────────────────────────────
    exportBtn.addEventListener('click', () => {
        const msgs = chatMessages.querySelectorAll('.message');
        if (msgs.length <= 1) { alert('No conversation to export yet.'); return; }
        let txt = `UNIVERSITY ENQUIRY PORTAL — CHAT EXPORT\nDate: ${new Date().toLocaleString()}\n${'='.repeat(52)}\n\n`;
        msgs.forEach(m => {
            const sender = m.classList.contains('user') ? 'STUDENT' : 'ASSISTANT';
            txt += `[${sender}]:\n${m.querySelector('.message-content').innerText}\n\n`;
        });
        const a = Object.assign(document.createElement('a'), {
            href: URL.createObjectURL(new Blob([txt], { type: 'text/plain' })),
            download: `university_chat_${Date.now()}.txt`
        });
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    });

    // ── Character Counter ─────────────────────────────────────────────────────
    userInput.addEventListener('input', function () {
        const len = this.value.length;
        charCounter.textContent = `${len}/200`;
        charCounter.style.color = len >= 180 ? 'var(--red)' : 'var(--txt-3)';
    });

    // ── Send on Enter / Button ────────────────────────────────────────────────
    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', e => { if (e.key === 'Enter') sendMessage(); });

    // ── Init Lucide ───────────────────────────────────────────────────────────
    if (window.lucide) lucide.createIcons();

    // ── Auto-focus (desktop only — avoid keyboard pop on mobile) ─────────────
    if (window.innerWidth >= 1024) userInput.focus();
});