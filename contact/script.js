// Select elements
const heroText = document.getElementById("heroText");
const fullText = "Welcome to the most reliable software services provider, where your expectations become your reality.";
let i = 0;
const scrollMessage = document.getElementById("scrollMessage");
const serviceCards = document.querySelectorAll(".service-card");
// HEADER HIDE/SHOW ON SCROLL
let lastScroll = 0;
const header = document.querySelector("header");


if (header) {
  document.addEventListener('mousemove', (e) => {
    if (e.clientY < 30) {  // mouse near top
      header.style.top = '0';
    } else {
      header.style.top = `-${header.offsetHeight}px`;
    }
  });
}


// 1️⃣ On load, fade in the hero text
window.addEventListener("load", () => {
  heroText.classList.add("show");
});

// 2️⃣ On scroll, show scroll message and services progressively
window.addEventListener("scroll", () => {
  const scrollY = window.scrollY;
  const windowHeight = window.innerHeight;

  // Show scroll message when user scrolls past hero
  if (scrollY > windowHeight * 0.3) {
    scrollMessage.classList.add("show");
  }

  // Show service cards one by one as they come into view
  serviceCards.forEach(card => {
    const cardTop = card.getBoundingClientRect().top;
    if (cardTop < window.innerHeight - 50) {
      card.classList.add("show");
    }
  });
});


document.addEventListener("DOMContentLoaded", () => {
  const chatHeader = document.getElementById("chatHeader");
  const chatBody = document.getElementById("chatBody");
  const chatInput = document.getElementById("chatInput");
  const chatSend = document.getElementById("chatSend");

  chatHeader.addEventListener("click", () => {
    chatBody.classList.toggle("show");
  });

  chatSend.addEventListener("click", () => {
    const message = chatInput.value.trim();
    if (message) {
      window.location.href = `mailto:moussamb1901@gmail.com?subject=Website%20Inquiry&body=${encodeURIComponent(message)}`;
      chatInput.value = "";
      alert("Message ready to send! Your email client will open.");
    }
  });
});

