import axios from 'axios'
import React, { Component } from 'react'

const api = axios.create({
    baseURL: "http://localhost:3000/contacts/"
})

export class ViewArticle extends Component {

    constructor(props) {
        super(props)
    
        this.state = {
             ArticleList : [],

        }
        this.FetchArticles = this.FetchArticles.bind(this)
    }
    componentDidMount(){
        this.FetchArticles()
    }
    FetchArticles = async () => {
        try{
            api.get("/")
            .then(response => {
                this.setState({
                    ArticleList:response.data
                })
                console.log("get data::", this.state.ArticleList)
            })
        }catch(error){
            console.log(error)
        }

        // fetch('http://127.0.0.1:8000/api/view_article/')
        // fetch("http://localhost:3000/contacts")
        // .then(response => response.json())
        // .then(data => {
        //     this.setState({
        //         ArticleList:data
        //     })
        //     console.log("data is",this.state.ArticleList)
        // })
    
    }
    CreateArticle = async() => {
        let res = await api.post("/", {"id":30, "name":"valli","email":"gangan3@gmail.com", "age":29})
        console.log("res",res)
        this.FetchArticles();
    }

    deleteData = async(id) => {
        console.log("id:::", id)
        let res = await api.delete(`${id}`)
        this.FetchArticles();

    }
        // console.log("id:::", id)
        // fetch('http://localhost:3000/contacts/'+id+'/',{
        //     method:'DELETE',
        //     body:JSON.stringify(this.state),
        // })
        // .then(response=>response)
        // .then(data => {
        //     if(data){
        //         this.FetchArticles();
        //     }
        // })

        UpdateData = async(id, val, age) => {
            let res = await api.patch(`${id}`, {name:val, age:age})
            this.FetchArticles();
        }
    
    render() {
        const ArticleData = this.state.ArticleList
        const rows = ArticleData.map(articles =>
            <tr class="table-active" key={articles}>
                <th scope="col">{articles.id}</th>
                <th scope="col">{articles.name}</th>
                <th scope="col">{articles.email}</th>
                <th scope="col">{articles.age}</th>
                <th> <button onClick={() => this.deleteData(articles.id)} className="btn btn-danger">DELETE</button> </th>
                <th><button onClick={this.CreateArticle} className="btn btn-primary">Create</button></th>
                <th><button onClick={() => this.UpdateData(articles.id, `${articles.name}a`, `${articles.age}3`)} className="btn btn-primary">Update</button></th>

            </tr>
            )
        return (
            <table class="table">
                <thead>
                <tr>
                <th scope="col">Title</th>
                <th scope="col">Author</th>
                <th scope="col">email</th>
                <th scope="col">date</th>
                <th scope="col">delete</th>
                <th scope="col">create</th>
                <th scope="col">update</th>



                </tr>

                </thead>
                <tbody>
                    {rows}
                </tbody>
               
                </table>
        )
    }
}

export default ViewArticle
