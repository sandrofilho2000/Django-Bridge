function handle_fields() {
  const question_type = document.querySelector('#id_question_model').value;
  if (question_type == 'multiple_choices' || question_type == 'select_box') {
    document.querySelector('#options-group').classList.add('active');
  } else {
    document.querySelector('#options-group').classList.remove('active');
  }
  if (question_type == 'star_rate') {
    document.querySelector('.field-min_text').classList.add('active');
    document.querySelector('.field-max_text').classList.add('active');
  } else {
    document.querySelector('.field-min_text').classList.remove('active');
    document.querySelector('.field-max_text').classList.remove('active');
  }
}

document.addEventListener('DOMContentLoaded', function () {
  handle_fields();
  document
    .querySelector('#id_question_model')
    .addEventListener('change', (e) => {
      handle_fields();
    });
});
