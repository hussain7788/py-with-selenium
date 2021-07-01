import React, { Component } from 'react'
import axios from 'axios'
import { green } from '@material-ui/core/colors'

const empApi = axios.create({
    baseURL: "http://localhost:3000/employee/"
})

export default class ViewEmp extends Component {

    constructor(props) {
        super(props)
        this.state = {
            id: "",
            emp_name: "",
            emp_email: "",
            emp_degn: "",
            empDataList: []
        }
        this.getEmp = this.getEmp.bind(this)
    }

    componentDidMount() {
        this.getEmp();
        this.deleteEmp();
        this.updateEmp();
    }

    getEmp = async () => {
        await empApi.get("/")
            .then(response => {
                this.setState({
                    empDataList: response.data
                })
                console.log("emp get data::", this.state.empDataList)
            })
    }
    deleteEmp(id){
        empApi.delete(`${id}`)
        this.getEmp();
    }
    updateEmp(id, val){
        let res = empApi.patch(`${id}`, {emp_name:val})
        console.log("update result", res)
        this.getEmp();

    }

    render() {
        const res = this.state.empDataList.map(emp => 
            <tr class="table-active" key={emp}>
                <th scope="col">{emp.id}</th>
                <th scope="col">{emp.emp_name}</th>
                <th scope="col">{emp.emp_email}</th>
                <th scope="col">{emp.emp_degn}</th>
                <th><button onClick={() => this.deleteEmp(emp.id)} className="btn btn-danger">Delete</button> </th>
                <th><button onClick={() => this.updateEmp(emp.id, `${emp.emp_name}s`)} className="btn btn-primary">Update</button> </th>
            </tr>
                )
        return (
            <div>
                <h2 style={{color:"blue",fontSize:"20px", textAlign:"center"}}> View Employee Details </h2>
                <table class="table">
                    <thead>
                        <tr>
                            <th scope="col">Id</th>
                            <th scope="col">Name</th>
                            <th scope="col">Email</th>
                            <th scope="col">Designation</th>
                            <th scope="col">delete</th>
                            <th scope="col">create</th>
                            <th scope="col">update</th>
                        </tr>

                    </thead>
                    <tbody>
                        {res}
                    </tbody>

                </table>
            </div>
        )
    }
}
