import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
    constructor() {
        super();
        this.state = {
            value: 'привіт',
            checked: true,
            option_value: ["Київ", "Одеса", "Вінниця", "Чернівці"],
            option: 'option1',
            texts: [],
            zd9_pagelist: ["Добрий вечір ми з України", "Слава Україні", "До перемоги!"],
            zd10_options: [],
            day: 0,
            month: 0,
            year: 1991
        };
    }

    //1
    //Записуємо value текстареа в this.state.value:
    handleChange(event) {
        this.setState({value: event.target.value});
    }

    //2-3
    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleCheckboxChange(event) {
        this.setState({checked: !this.state.checked});
    }

    //4
    handleSelectChange(event) {
        this.setState({value: event.target.value});
    }

    //5
    handleRadioChange(event) {
        this.setState({option: event.target.value});
    }

    //6
    pushbackToTexts() {
        this.state.texts.push(this.state.value);
        this.setState({texts: this.state.texts});
    }

    //10
    pushbackToOptions() {
        this.state.zd10_options.push(this.state.value);
        this.setState({zd10_options: this.state.texts});
    }

    //12
    handleSelectChangeDay(event) {
        this.setState({day: event.target.value});
    }
    handleSelectChangeMonth(event) {
        this.setState({month: event.target.value});
    }
    handleSelectChangeYear(event) {
        this.setState({year: event.target.value});
    }

    getWeekDay() {
        let days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        let date = new Date(this.state.year, this.state.month-1, this.state.day);
        return days[date.getDay()];
    }


    render() {
        const option = this.state.option_value.map((item, index) => {
            return <option key={index} value={item}>{item}</option>;
        });

        const page6 = this.state.texts.map((item, index) => {
            return <p>{item}</p>;
        });

        const page9 = <p> {this.state.zd9_pagelist[this.state.value - 1]} </p>;
        
        const zd10_option = this.state.zd10_options.map((item, index) => {
            return <option key={index} value={index}>{item}</option>;
        });

        var daylist = [];
        for (let i = 1; i <= 31; i++) {
            daylist.push(i);
        }
        var monthlist = [];
        for (let i = 1; i <= 12; i++) {
            monthlist.push(i);
        }
        var yearlist = [];
        for (let i = 1991; i <= 2023; i++) {
            yearlist.push(i);
        }


        const zd12_option_day = daylist.map((item, index) => {
            return <option key={index} value={index}>{item}</option>;
        });
        const zd12_option_month = monthlist.map((item, index) => {
            return <option key={index} value={index}>{item}</option>;
        });
        const zd12_option_year = yearlist.map((item, index) => {
            return <option key={index} value={index}>{item}</option>;
        });


        return (
            <div>
        Завдання 1
            <p>Головний абзац: <br/> {this.state.value}</p>
            <textarea value={this.state.value} onChange={this.handleChange.bind(this)}/>
            <hr/>
        Завдання 2-3
            <input type="checkbox" checked={this.state.checked} onChange={this.handleChange.bind(this)}/>
            <p>Стан: {this.state.checked ? 'відмічено' : 'не відмічено'}</p>
            <hr/>
        Завдання 4
            <br></br>
            <select value={this.state.value} onChange={this.handleSelectChange.bind(this)}>
                {option}
            </select>
            <p>{this.state.value}</p>
            <hr/>
        Завдання 5
            <p>Ваш вибір: {this.state.option}</p>
            <input name="lang" type="radio" value="option1" checked={this.state.option == 'option1'} onChange={this.handleRadioChange.bind(this)}/>
            <input name="lang" type="radio" value="option2" checked={this.state.option == 'option2'} onChange={this.handleRadioChange.bind(this)}/>
            <input name="lang" type="radio" value="option3" checked={this.state.option == 'option3'} onChange={this.handleRadioChange.bind(this)}/>
            <hr/>
        Завдання 6
            <br/>
            <textarea value={this.state.value} onChange={this.handleChange.bind(this)}/>
            <br/>
            <button onClick={this.pushbackToTexts.bind(this)}>Push back</button>
            <br/>
            texts:
            <br/>
            {page6}
            <hr/>
        Завдання 7
            <p style={{backgroundColor: this.state.value}}>колір</p>
                <select value={this.state.value} onChange={this.handleSelectChange.bind(this)}>
                    <option>white</option>
                    <option>black</option>
                    <option>red</option>
                    <option>blue</option>
                    <option>yellow</option>
                    <option>pink</option>
                </select>
                <hr/>
        Завдання 8
        <input type="checkbox" checked={this.state.checked} onChange={this.handleCheckboxChange.bind(this)}/>
        <select value={this.state.checked} onChange={this.handleSelectChange.bind(this)}>
                    <option>позначено</option>
                    <option>не позначено</option>
        </select>
        <hr/>
        Завдання 9
        <br/>
            <select value={this.state.value} onChange={this.handleSelectChange.bind(this)}>
                <option>1</option>
                <option>2</option>
                <option>3</option>
            </select>
            <br/>
            {page9}
            <hr/>
        Завдання 10
        <br/>
        <p>Введіть тільки текст(цифра не буде рахуватись)</p>
        <input name="lang" onChange={this.handleChange.bind(this)}/>
            <button onClick={this.pushbackToOptions.bind(this)}>Push back</button>
            <select value={this.state.value}>
                {zd10_option}
            </select>
        <hr/>
        Завдання 11
        <br/>
        <input type="checkbox" checked={this.state.checked} onChange={this.handleCheckboxChange.bind(this)}/>
            <input name="lang" disabled={!this.state.checked}/>
            <hr/>
        Завдання 12
        <br/>
        <select value={this.state.day} onChange={this.handleSelectChangeDay.bind(this)}>
                    {zd12_option_day}
                </select>
                <select value={this.state.month} onChange={this.handleSelectChangeMonth.bind(this)}>
                    {zd12_option_month}
                </select>
                <select value={this.state.year} onChange={this.handleSelectChangeYear.bind(this)}>
                    {zd12_option_year}
                </select>
                <p>{this.getWeekDay()}</p>
        </div>
        );
    }
}

ReactDOM.render(<App/>, document.getElementById("root"));