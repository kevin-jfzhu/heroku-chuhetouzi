var search_box = document.getElementById('search_box');
var search_btn = document.getElementById('search_button');

function load_search_value() {
    let time_string = search_box.value;

    if (time_string !== '') {
        if (moment(time_string).isValid()) {
            console.log(search_box.value);
        } else {
            alert('您输入的起始日期有误，请重新输入')
        }
    }
}

search_btn.addEventListener('click', load_search_value);
