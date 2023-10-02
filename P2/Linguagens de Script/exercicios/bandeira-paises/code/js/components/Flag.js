export default function Flag(flag) {
    return `
    <div class="flag col-2 my-2 text-center">
    <img src="./imgs/flags/${flag.id}.png" alt="${flag.image}">
    <p>${flag.name}</p>
    </div>
    `
}