const yesButton = document.getElementById("yes-button");
const noButton = document.getElementById("no-button");
const responseContainer = document.getElementById("response");
const message = document.getElementById("message");

yesButton.addEventListener("click", function () {
    responseContainer.style.display = "block";
    message.innerText = "You've made me the happiest person in the world! I love you forever and always.";
    yesButton.style.display = "none";
    noButton.style.display = "none";
});

noButton.addEventListener("click", function () {
    responseContainer.style.display = "block";
    message.innerText = "I'll keep trying until you say yes. Take your time, my love.";
    noButton.style.position = "absolute";

    // Calculate a random position for the "No" button
    const maxX = window.innerWidth - noButton.offsetWidth;
    const maxY = window.innerHeight - noButton.offsetHeight;
    const randomX = Math.floor(Math.random() * maxX);
    const randomY = Math.floor(Math.random() * maxY);

    noButton.style.left = randomX + "px";
    noButton.style.top = randomY + "px";
});