/* main.js */

document.addEventListener("DOMContentLoaded", function () {
  // Management of radio buttons
  const radios = document.querySelectorAll(QUERY_RADIOS);
  manageRadios(radios);
});

function manageRadios(radios) {
  radios.forEach((radio) => {
    radio.addEventListener("click", () => {
      radios.forEach((otherRadio) => {
        otherRadio.classList.remove(...Object.values(RADIO_SELECTED_MAPPING));
      });

      radio.classList.add("radio-disabled");

      const answer = expressAnswer(radio.classList);
      document.getElementById(QUERY_INPUT_ANSWER).value = answer;

      for (const rType of RADIO_TYPES) {
        if (radio.classList.contains(rType)) {
          radio.classList.add(RADIO_SELECTED_MAPPING[rType]);
          break;
        }
      }
    });
  });
}

function expressAnswer(radioClassList) {
  for (const className of radioClassList) {
    if (className in ANSWER_MAPPING) {
      return ANSWER_MAPPING[className];
    }
  }
  return "";
}
