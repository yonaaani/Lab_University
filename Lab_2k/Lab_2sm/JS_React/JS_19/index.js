import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
    constructor() {
        super();
        this.state = {
            name: 'Іван', age: 25, show: false,
            name_mas: ['Коля', 'Василь', 'Петро', 'Іван', 'Дмитро'],
            input5: 'start',
            input6: 'start6',
            input7: '',
            year: 2023,
            input8: '',
            text9: '',
            text9_2: '',
            text10: '',
            text10_1: '',
            text10_2: '',
            pib: ['', '', '', ''],
            inputName12: '',
            hrefs: [
                {href: '1.html', text: 'посилання 1'},
                {href: '2.html', text: 'посилання 2'},
                {href: '3.html', text: 'посилання 3'},
            ],
            href: '',
            textHref: '',
            idForDel: '',
            users: [
                {name: 'Коля', age: 30},
                {name: 'Василь', age: 40},
                {name: 'Петро', age: 50},
            ],
            users_name: '',
            users_age: ''

        };
    }

    // 1 - 4
    addItem(text = 'пункт') {
        this.state.name_mas.push(text); //змінюємо стейт напряму
        this.setState({name_mas: this.state.name_mas}); //застосовуємо зміни
    }

    dellItem() {
        this.state.name_mas.pop(); //змінюємо стейт напряму
        this.setState({name_mas: this.state.name_mas}); //застосовуємо зміни
    }

    dellItemId(id) {
        this.state.name_mas.splice(id, 1); //змінюємо стейт напряму
        this.setState({name_mas: this.state.name_mas}); //застосовуємо зміни
    }

    //5
    changeInput(event) {
        this.setState({input5: event.target.value});
    }

    //6
    changeInput2(event) {
        this.setState({input6: event.target.value});
    }

    //7
    changeInput3(event) {
        if (Number.isInteger(parseInt(event.target.value, 10))) {
            this.setState({input7: parseInt(event.target.value, 10)});
        }
        if (event.target.value == '') {
            this.setState({input7: event.target.value});
        }
    }

    //8
    changeInput4(event) {
        this.setState({input8: event.target.value});
    }

    //9
    changeText9(event) {
        this.setState({text9: event.target.value});
    }

    SubmitText9(event) {
        this.setState({text9_2: this.state.text9});
        event.preventDefault(); // відміняємо надсилання форми
    }

    //10
    changeText10(event) {
        this.setState({text10: event.target.value});
    }

    changeText10_1(event) {
        this.setState({text10_1: event.target.value});
    }

    SubmitText10(event) {
        this.setState({text10_2: parseInt(this.state.text10) + parseInt(this.state.text10_1)});
        event.preventDefault(); // відміняємо надсилання форми
    }

    //11
    changePib(id, event) {
        this.state.pib[id] = event.target.value;
        this.setState({pib: this.state.pib});
    }

    SubmitPib(event) {
        this.state.pib[3] = this.state.pib[0] + " " + this.state.pib[1] + " " + this.state.pib[2];
        this.setState({pib: this.state.pib});
        event.preventDefault(); // відміняємо надсилання форми
    }

    //12-13
    changeInputName(event) {
        this.setState({inputName12: event.target.value});
    }

    addItem2(event) {
        this.addItem(this.state.inputName12);
        event.preventDefault(); // відміняємо надсилання форми
    }

    // 14
    SubmitHref(event) {
        this.state.hrefs.push({href: this.state.href, text: this.state.hrefText});
        this.setState({hrefs: this.state.hrefs});
        event.preventDefault(); // відміняємо надсилання форми
    }

    changeHref(event) {
        this.state.href = event.target.value;
        this.setState({href: this.state.href});
    }

    changeHrefText(event) {
        this.state.hrefText = event.target.value;
        this.setState({hrefText: this.state.hrefText});
    }

    //15
    changeIdForDel(event) {
        this.state.idForDel = event.target.value;
        this.setState({idForDel: this.state.idForDel});
    }
    SubmitIdForDel(event) {
        this.dellItemId(this.state.idForDel);
        event.preventDefault(); // відміняємо надсилання форми
    }

    //16
    SubmitPushToUsers(event) {
        this.state.users.push({name: this.state.users_name, age: this.state.users_age});
        this.setState({users: this.state.users});
        event.preventDefault(); // відміняємо надсилання форми
    }
    changeUsers_name(event) {
        this.state.users_name = event.target.value;
        this.setState({users_name: this.state.users_name});
    }

    changeUsers_age(event) {
        this.state.users_age = event.target.value;
        this.setState({users_age: this.state.users_age});
    }


    render() {
        const pib = this.state.input8.split(" ");

        const rez9 = this.state.name_mas.map((item, index) => {
            return <li key={index}>
                {item}
                <button onClick={this.dellItemId.bind(this, index)}>
                    del
                </button>
            </li>;
        });

        const rez14 = this.state.hrefs.map(function (item, index) {
            return <li><a href={item.href}> {item.text}</a></li>;
        });

        const rez15 = this.state.name_mas.map((item, index) => {
            return <li key={index}>
                {item}
            </li>;
        });

        const rez16 = this.state.users.map((item, index) => {
            return <tr>
                <td> {item.name} </td><td> {item.age} </td>
            </tr>;
        });


        return (
            <div>
              Завдання 1-4
                <div>
                    <ul>
                        {rez9}
                    </ul>
                    <button onClick={this.dellItem.bind(this)}>Видалити</button>
                </div>
                <hr/>

              Завдання 5
                <div>
                    <input value={this.state.input5} onChange={this.changeInput.bind(this)}/>
                    <p>
                        {this.state.input5}
                    </p>
                </div>
                <hr/>
          
              Завдання 6
                <div>
                    <input value={this.state.input6} onChange={this.changeInput2.bind(this)}/>
                    <p>
                        {this.state.input6.toUpperCase()} 
                    </p>
                </div>
                <hr/>

              Завдання 7
                <div>
                    <input value={this.state.input7} onChange={this.changeInput3.bind(this)}/>
                    <p>
                        Вік: {this.state.input7}
                    </p>
                    <p>
                      Рік народження: {this.state.year - this.state.input7}
                    </p>
                </div>
                <hr/>

                <div>
                    <p>Завдання 8</p>
                    Введіть ПІБ
                    <br/>
                    <input value={this.state.input8} onChange={this.changeInput4.bind(this)}/>
                    <p>
                        Прізвище: {pib[0]}
                    </p>
                    <p>
                        Ім'я: {pib[1]}
                    </p>
                    <p>
                        По батькові: {pib[2]}
                    </p>
                </div>
                <hr/>

               Завдання 9
                <form onSubmit={this.SubmitText9.bind(this)}>
                    <input value={this.state.text9} onChange={this.changeText9.bind(this)}/>
                    <input type="submit"/>
                    <p>{this.state.text9_2}</p>
                </form>
                <hr/>

               Завдання 10
               <p>Введіть числа</p>
                <form onSubmit={this.SubmitText10.bind(this)}>
                    <input value={this.state.text10} onChange={this.changeText10.bind(this)}/>
                    <input value={this.state.text10_1} onChange={this.changeText10_1.bind(this)}/>
                    <input type="submit"/>
                    <p>{this.state.text10_2}</p>
                </form>
                <hr/>

                Завдання 11
                <p>Введіть ПІБ</p>
                <form onSubmit={this.SubmitPib.bind(this)}>
                    <input onChange={this.changePib.bind(this, 0)}/>
                    <input onChange={this.changePib.bind(this, 1)}/>
                    <input onChange={this.changePib.bind(this, 2)}/>
                    <input type="submit"/>
                    <p>{this.state.pib[3]}</p>
                </form>
                <hr/>

                Завдання 12-13
                <form onSubmit={this.addItem2.bind(this)}>
                    <ul>
                        {rez9}
                    </ul>
                    <input value={this.state.inputName12} onChange={this.changeInputName.bind(this)}/>
                    <input type="submit"/>
                </form>
                <hr/>

                Завдання 14
                <p>Введіть посилання + текст</p>
                <form onSubmit={this.SubmitHref.bind(this)}>
                    <ul>
                        {rez14}
                    </ul>
                    <input value={this.state.href} onChange={this.changeHref.bind(this)}/>
                    <input value={this.state.hrefText} onChange={this.changeHrefText.bind(this)}/>
                    <input type="submit"/>
                </form>
                <hr/>

                Завдання 15
                <form onSubmit={this.SubmitIdForDel.bind(this)}>
                    <ul>
                        {rez15}
                    </ul>
                    <input value={this.state.idForDel} onChange={this.changeIdForDel.bind(this)}/>
                    <input type="submit"/>
                </form>
                <hr/>

                Завдання 16
                <table>
                    {rez16}
                </table>
                <form onSubmit={this.SubmitPushToUsers.bind(this)}>
                    <input value={this.state.users_name} onChange={this.changeUsers_name.bind(this)}/>
                    <input value={this.state.users_age} onChange={this.changeUsers_age.bind(this)}/>
                    <input type="submit"/>
                </form>

            </div>
        );
    }
}

ReactDOM.render(<App/>, document.getElementById("root"));