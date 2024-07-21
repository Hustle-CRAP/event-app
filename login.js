document.addEventListener('DOMContentLoaded', () => {
  const loginText = document.querySelector(".title-text .login");
  const loginForm = document.querySelector("#loginForm");
  const signupForm = document.querySelector("#signupForm");
  const loginBtn = document.querySelector("label.login");
  const signupBtn = document.querySelector("label.signup");
  const signupLink = document.querySelector(".signup-link a");

  signupBtn.addEventListener('click', () => {
    loginForm.style.marginLeft = "-50%";
    loginText.style.marginLeft = "-50%";
  });

  loginBtn.addEventListener('click', () => {
    loginForm.style.marginLeft = "0%";
    loginText.style.marginLeft = "0%";
  });

  signupLink.addEventListener('click', (e) => {
    e.preventDefault();
    signupBtn.click();
  });

  // Validation functions
  function validatePassword(password) {
    const pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return pattern.test(password);
  }

  function validateForms() {
    const loginEmail = document.querySelector("#loginEmail");
    const loginPassword = document.querySelector("#loginPassword");
    const signupEmail = document.querySelector("#signupEmail");
    const signupPassword = document.querySelector("#signupPassword");
    const confirmPassword = document.querySelector("#confirmPassword");

    // Login form validation
    loginForm.addEventListener('submit', (e) => {
      if (!validatePassword(loginPassword.value)) {
        e.preventDefault();
        alert("Password must contain uppercase, lowercase, digits, special characters, and be at least 8 characters long.");
      }
    });

    // Signup form validation
    signupForm.addEventListener('submit', (e) => {
      if (!validatePassword(signupPassword.value)) {
        e.preventDefault();
        alert("Password must contain uppercase, lowercase, digits, special characters, and be at least 8 characters long.");
      } else if (signupPassword.value !== confirmPassword.value) {
        e.preventDefault();
        alert("Passwords do not match.");
      }
    });
  }

  validateForms();
});
