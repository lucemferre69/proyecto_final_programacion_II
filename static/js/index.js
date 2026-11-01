const btnEncendido = document.querySelector(".c1");
const muestra = document.querySelector(".muestra");
const pantalla = document.querySelector(".pantalla");
const c2 = document.querySelector(".c2");
const c3 = document.querySelector(".c3");
const c4 = document.querySelector(".c4");
const cards = document.querySelectorAll(".card");
const card1 = document.querySelector(".card");
const modificar = document.querySelector(".modificar");
const eliminar = document.querySelector(".eliminar");

let encendido = false
if (window.location.href.endsWith('/') == false){
  encendido = true
}

if (encendido){
    btnEncendido.style.backgroundColor = '#3494F3'
    c2.style.backgroundColor = 'red';
    c3.style.backgroundColor = 'yellow';
    c4.style.backgroundColor = 'green';
    pantalla.style.animation = 'mostrar-pantalla 1s forwards';
}

btnEncendido.addEventListener('click', () =>{
    if (encendido){
    window.location.href = `/`;
    } else {
    window.location.href = '/menu';
    }
})

const btnX1 = document.querySelector(".x1");
const btnX2 = document.querySelector(".x2");
const btnX3 = document.querySelector(".x3");
const btnX4 = document.querySelector(".x4");
const contAgrupar = document.querySelector(".botones-agrupar");
const btnAgrupar = contAgrupar.querySelectorAll("button");

btnAgrupar.forEach((button) =>{
    button.addEventListener('click', () => {
      let fr = '';
        for (let i = 0; i < button.dataset.num; i++) {
          fr += ' 1fr';
        }
      muestra.style.gridTemplateColumns = fr;
    })
})


function selectCard(index) {
  cards.forEach(card => card.classList.remove('selected'));

  currentIndex = index;
  cards[currentIndex].classList.add('selected');
  cards[currentIndex].focus();
  let card = document.querySelector('.selected');
  let idSelected = card.dataset.id;
  modificar.href = `/modificar/${idSelected}`;
  eliminar.href = `/eliminar/${idSelected}`;
}

cards.forEach((card, index) => {
  card.addEventListener('click', () => {
    selectCard(index);
  });
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'ArrowRight') {
    if (currentIndex < cards.length - 1) {
      selectCard(currentIndex + 1);
    }
  } else if (event.key === 'ArrowLeft') {
    if (currentIndex > 0) {
      selectCard(currentIndex - 1);
    }
  }
});

if (window.location.href.includes('modificar')){
  muestra.style.display = 'flex';
  
}

const select = document.querySelectorAll("select")

select.forEach((select) =>{
  const opciones = select.querySelectorAll("option");
  opciones.forEach((option) => {
  if (select.classList.contains(option.value)){
    option.selected = true;
  }
  option.classList.add(option.value);
  if (option.selected){
    let selectedOption = option;
    return selectedOption
  }
});
  select.addEventListener('change', (event) => {
    select.classList.remove(select.classList.item(1));
    select.classList.add(event.target.value);
  })
})

const btnTipo2 = document.querySelector(".btn-tipo-2");
const contSelect = document.querySelector(".cont-select");
const select2 = contSelect.querySelector(".tipo_2")
const inputHidden = document.querySelector('.input-hidden');
inputHidden.value = '';

btnTipo2.addEventListener('click', () =>{
  if (btnTipo2.classList.contains("mas")){
    select2.name = 'tipo_2';
    inputHidden.name = ''
    btnTipo2.classList.add("menos");
    btnTipo2.classList.remove("mas");
    btnTipo2.textContent = "-";
  } else {
    select2.name = '';
    inputHidden.name = 'tipo_2';
    btnTipo2.classList.add("mas");
    btnTipo2.classList.remove("menos");
    btnTipo2.textContent = "+";
  }
  select2.classList.toggle('hidden');
})