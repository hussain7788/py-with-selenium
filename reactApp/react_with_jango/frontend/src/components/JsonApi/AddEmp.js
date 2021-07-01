import React, { Component } from 'react'
import axios from 'axios'

const empApi = axios.create({
    baseURL: "http://localhost:3000/employee/"
})

export default class AddEmp extends Component {
    constructor(props) {
        super(props)
        this.state = {
            id: "",
            emp_name: "",
            emp_email: "",
            emp_degn: "",
            emp_data: []
        }
        this.changeHandler = this.changeHandler.bind(this)
        this.addEmp = this.addEmp.bind(this)
    }
    changeHandler(e) {
        this.setState({
            [e.target.name]: e.target.value
        })
    }
    componentDidMount() {
        this.getEmpData();
    }
    getEmpData() {
        empApi.get("/")
            .then(response => {
                this.setState({
                    emp_data: response.data
                })
                console.log("new::", this.state.emp_data)
            })
    }

    addEmp = async () => {
        const result = this.state.emp_data
        let res = await empApi.post("/", this.state)
        console.log("emp add result", res.data)
        this.setState({
            id: "",
            emp_name: "",
            emp_email: "",
            emp_degn: ""
        })

    }

    render() {
        return (
            <div>
                <h1> Add Employee Form</h1>
                <div>
                    <input type="text" placeholder="empId" name="id" value={this.state.id} onChange={this.changeHandler} />
                </div>
                <div>
                    <input type="text" placeholder="empName" name="emp_name" value={this.state.emp_name} onChange={this.changeHandler} />
                    <span id="s1">.</span>
                </div>
                <div>
                    <input type="text" placeholder="empEmail" name="emp_email" value={this.state.emp_email} onChange={this.changeHandler} />
                    <span id="s2">.</span>
                </div>
                <div>
                    <input type="text" placeholder="empDegn" name="emp_degn" value={this.state.emp_degn} onChange={this.changeHandler} />
                </div>
                <div>
                    <button onClick={this.addEmp} className="btn btn-primary">Add Emp</button>
                </div>
            </div >

        )
    }
}
