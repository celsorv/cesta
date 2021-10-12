(function(win, doc) {
	'use strict';

	// verifica se o usuário realmente quer deletar o dado
	if (doc.querySelector('.btnDel')) {
		let btnDel = doc.querySelectorAll('.btnDel');
		for (let i=0; i < btnDel.length; i++) {
			btnDel[i].addEventListener('click', function(event) {
				if (confirm('Deseja mesmo apagar este dado?')) {
					return true;
				} else {
					event.preventDefault();
				}
			});
		}
	}
/*
	// Ajax do form
	if (doc.querySelector('#form')) {
		let form = doc.querySelector('#form');
		function sendForm(event) {
			event.preventDefault();
			let data = new FormData(form);
			let ajax = new XMLHttpRequest();
			let token = doc.querySelectorAll('input')[0].value;
			ajax.open('POST', form.action);
			ajax.setRequestHeader('X-CSRF-TOKEN', token);
			ajax.onreadystatechange = function() {
				if (ajax.status === 200 && ajax.readyState === 4) {
					let result = doc.querySelector('#result');
					result.innerHTML = 'Operação realizada com sucesso!';
					result.classList.add('alert');
					result.classList.add('alert-success');
				}
			}
			ajax.send(data);
			form.reset();
		}
		form.addEventListener('submit', sendForm, false);
	}
*/
})(window, document);
