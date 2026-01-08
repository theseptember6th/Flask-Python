const form = document.getElementById("note-form");
const input = document.getElementById("note-input");
const list = document.getElementById("notes-list");

if (form) {
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const text = input.value.trim();
    if (!text) return;

    const li = document.createElement("li");
    li.innerHTML = `
      <span>${text}</span>
      <span class="delete-btn">✖</span>
    `;

    li.querySelector(".delete-btn").onclick = () => li.remove();
    list.appendChild(li);
    input.value = "";
  });
}
