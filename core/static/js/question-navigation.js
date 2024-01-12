/* question-navigation.js */

const CSS_INVISIBLE = "d-none";

var currentIndex = 0;

function handleQuestionNavigation(offset) {
  const currentQuestion = document.querySelector(`#question-${currentIndex}`);
  const nextQuestion = document.querySelector(
    `#question-${currentIndex + offset}`
  );

  if (!nextQuestion) {
    return;
  }

  let radios = document.querySelectorAll(QUERY_RADIOS);

  radios.forEach((r) => {
    r.removeEventListener("click", () => {});
  });

  currentQuestion.classList.add(CSS_INVISIBLE);
  nextQuestion.classList.remove(CSS_INVISIBLE);

  radios = document.querySelectorAll(QUERY_RADIOS);

  handleAvailableRadios(radios);

  currentIndex += offset;
}

function prevQuestion() {
  handleQuestionNavigation(-1);
}

function nextQuestion() {
  handleQuestionNavigation(1);
}
