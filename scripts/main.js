const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
const dropdown = document.querySelector('.dropdown');

hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});

// Optional: Click to expand dropdown in mobile
dropdown.addEventListener('click', (e) => {
  if (window.innerWidth <= 768) {
    e.preventDefault();
    dropdown.classList.toggle('open');
  }
});