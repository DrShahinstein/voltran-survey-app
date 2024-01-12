/* main.js */

document.addEventListener("DOMContentLoaded", function () {
  // Take out the invisibility of the first question
  document.querySelector("#question-0").classList.remove("d-none");

  // Management of radio buttons
  const radios = document.querySelectorAll(QUERY_RADIOS);
  handleAvailableRadios(radios);
});

function handleAvailableRadios(radios) {
  radios.forEach((radio) => {
    radio.addEventListener("click", () => {
      radios.forEach((otherRadio) => {
        otherRadio.classList.remove(...Object.values(selectedClassMap));
      });

      radio.classList.add("radio-disabled");

      for (const rType of radioTypes) {
        if (radio.classList.contains(rType)) {
          radio.classList.add(selectedClassMap[rType]);
          break;
        }
      }
    });
  });
}
