import React, { Component } from 'react'

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
    FetchArticles(){

        fetch('http://127.0.0.1:8000/api/view_article/')
        .then(response => response.json())
        .then(data => {
            this.setState({
                ArticleList:data
            })
            console.log("data is",ArticleList)
        })
    }
    
    render() {
        const ArticleData = this.state.ArticleList
        const rows = ArticleData.map(articles =>
            <tr class="table-active" key={articles}>
                <th scope="col">{articles.title}</th>
                <th scope="col">{articles.author}</th>
                <th scope="col">{articles.email}</th>
                <th scope="col">{articles.date}</th>
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
