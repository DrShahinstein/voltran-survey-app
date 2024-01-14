/* helpers.js */

const RADIO_TYPES = ["radio-agree", "radio-disagree", "radio-neutral"];

const RADIO_SELECTED_MAPPING = {
  "radio-agree": "radio-agree-selected",
  "radio-disagree": "radio-disagree-selected",
  "radio-neutral": "radio-neutral-selected",
};

const QUERY_RADIOS = ".radio-span";

const QUERY_INPUT_ANSWER = "input-selected-answer";

const ANSWER_MAPPING = {
  "radio-0": "strongly agree",
  "radio-1": "agree",
  "radio-2": "neutral",
  "radio-3": "disagree",
  "radio-4": "strongly disagree",
};
