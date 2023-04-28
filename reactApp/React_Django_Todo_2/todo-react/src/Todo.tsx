import React, { useEffect, useState } from "react";
import {post, get, del, getCancelToken} from './backendinterface';
import { AxiosResponse } from "axios";

const ENDPOINT = 'http://127.0.0.1:8000/todo/'

interface ITodoItems {
    id: number,
    name: string,
    created: string,
    completed: boolean
}

interface ITodoItemsFetch extends AxiosResponse{
    data: ITodoItems[]
  }

  interface ITodoItemsCreate extends AxiosResponse{
    data: ITodoItems
  }

function Todo() {

    const [todoListData, settodoListData] = React.useState<ITodoItems[]>([]);
    const [taskName, setTaskName] = React.useState('');
    const cancelTokenSource = React.useRef(getCancelToken());
    const [filterValue, setfilterValue] = React.useState('')


    React.useEffect(() => {
        const request_response = get(ENDPOINT, cancelTokenSource.current.token) as Promise<ITodoItemsFetch>;
        request_response.then((response) => {
            console.log("data", response.data)
            settodoListData(response.data)
        })

    }, [])

    function addTaskItems() {
        console.log('clicked')
        let query_params = {
            section: 'create'
        }
        let formData = new FormData();
        formData.append("task_name", taskName)
        let request_response = post(ENDPOINT, formData, cancelTokenSource.current.token, query_params) as Promise<ITodoItemsCreate>
        request_response.then(response => {
            console.log("added data", response.data)
           settodoListData((prevItemsListData) => {
            let newItemsListData = [...prevItemsListData, response.data]
            return newItemsListData;
           })
        })


    }

    function todoFilter(value: string){

        let query_params = {
            section: 'filter'
        }
        let formData = new FormData()
        formData.append('filter_value', value)
        let request_response = post(ENDPOINT, formData, cancelTokenSource.current.token, query_params) as Promise<ITodoItemsFetch>;
        request_response.then((response) => {
            settodoListData(response.data)
        })
        console.log(`${value}`)

    }

    function todoAdd() {
        return (
            <React.Fragment>
                <h3>Add Todo Items</h3>
                <input type="text" value={taskName} onChange={(e) => setTaskName(e.target.value)} placeholder="Task Name"/>
                <button type="submit" onClick={addTaskItems}>Add Task</button>

                <div>
                    <select value={filterValue} onChange={(e) => todoFilter(e.target.value)}>
                        <option value=''>filter task</option>
                        <option value='all_tasks'>All Tasks</option>
                        <option value='pending_tasks'>Pending Tasks</option>
                        <option value='completed_tasks'>Completed Tasks</option>
                    </select>
                
                </div>

            </React.Fragment>
        )
    }

    function markComplete(id: number) {
        console.log("markComplete id", id)
        let query_params = {
            section: 'mark_completed'
        }
        let formdata = new FormData()
        formdata.append('task_id', id.toString())
        let request_response  = post(ENDPOINT, formdata, cancelTokenSource.current.token, query_params) as Promise<ITodoItemsCreate>;
        request_response.then((response) => {
            console.log(response.data)
            settodoListData((prevItemsListData) => {
                let newItemsListData = [...prevItemsListData]
                let replcaeIndex = newItemsListData.findIndex((item) => item.id == id)
                console.log("todoListData", todoListData)
                console.log("findindex", replcaeIndex)
                newItemsListData[replcaeIndex] = response.data
                return newItemsListData;
                
            })
        })

    }

    function deleteItem(id: number){
        console.log("delete id", id)
        let query_params = {}
        let url = ENDPOINT + id 
        let request_response = del(url, query_params)
        request_response.then((response) => {
            console.log("delete response", response.data)
            settodoListData(response.data)
        })
    }

    function showAllTodoItems() {
        return (
            <ul>
                {todoListData.map((item) => {
                    return (
                        <li key={item.id}>
                            <ul>
                            <li>Task Name: {item.name}</li>
                            <li>Task Created on: {item.created}</li>

                            {(() => {
                                if (item.completed) {
                                    return <li style={{color:"blue"}}>Task is Complated</li>
                                }
                                else{
                                    return (
                                        <li>
                                            <p style={{color:'red'}}>Not Completed</p>
                                            <input type="checkbox" onClick={(e) => markComplete(item.id)} />
                                        </li>
                                    )
                                }
                            })()}
                            <button type="submit" onClick={(e) => deleteItem(item.id)}>delete</button>
                            </ul>
                        </li>
                    )
                })}
            </ul>
        )
    }

    return (
        <div className="Todo"> 
            {todoAdd()}
            {showAllTodoItems()}
        </div>
    );

}


export default Todo;