import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Form, Button } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Loader from '../components/Loader'
import Message from '../components/Message'
import FormContainer from '../components/FormContainer'
import { getUserDetails, updateUser } from '../actions/userActions'
import { USER_UPDATE_RESET } from '../constants/userConstants'
import ApexChart from 'react-apexcharts';
import {
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
  } from 'recharts';
  import {
    Chart,
  } from 'chart.js';
  const da = {
    labels: [
      'Red',
      'Green',
      'Yellow',
      'Grey',
      'Blue'
    ],
    datasets: [{
      label: 'My First Dataset',
      data: [11, 16, 7, 3, 14],
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(75, 192, 192)',
        'rgb(255, 205, 86)',
        'rgb(201, 203, 207)',
        'rgb(54, 162, 235)'
      ]
    }]
  };
  const data = [
    {
      name: '2022-08-22', 긍정: 40, 부정: 24, amt: 24,
    },
    {
      name: '2022-08-23', 긍정: 30, 부정: 98, amt: 22,
    },
    {
      name: '2022-08-24', 긍정: 20, 부정: 98, amt: 22,
    },
    {
      name: '2022-08-25', 긍정: 27, 부정: 38, amt: 20,
    },
    {
      name: '2022-08-26', 긍정: 18, 부정: 48, amt: 21,
    },
    {
      name: '2022-08-27', 긍정: 23, 부정: 38, amt: 25,
    },
    {
      name: '2022-08-28', 긍정: 34, 부정: 43, amt: 21,
    },
  ];
  
function GraphicScreen({ history }) {
    return (
        <div>
            <Link to='/admin/userlist'>
                Go Back
            </Link>

            <FormContainer>
                <h1>소비자 현황</h1>
                <LineChart
                    width={500}
                    height={300}
                    data={data}
                    margin={{
                    top: 5, right: 30, left: 20, bottom: 5,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Line type="monotone" dataKey="부정" stroke="#8884d8" activeDot={{ r: 8 }} />
                    <Line type="monotone" dataKey="긍정" stroke="#82ca9d" />
                </LineChart>
               
                <Button
                                                    className='btn-block'
                                                    type='button'>
                                                    E-mail 전송
                                                </Button>

            </FormContainer >
        </div>

    )
}

export default GraphicScreen