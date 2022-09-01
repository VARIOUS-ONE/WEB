// import axios from 'axios'
// import React, { useState, useEffect } from 'react'
// import { LinkContainer } from 'react-router-bootstrap'
// import { Table, Button } from 'react-bootstrap'
// import { useDispatch, useSelector } from 'react-redux'
// import Loader from '../components/Loader'
// import Message from '../components/Message'
// import { listUsers, deleteUser } from '../actions/blackActions'


// function BlackListScreen({ history }){

//     var blacklist = [{"model": "base.blacklist", "pk": 2, "fields": {"score": 0, "review": "포장이 겉박스도 없고고 너무 무성의사네요 머 제품은 이상 없겠지만 사소한 부분도 챙길줄 아는 판매자 원합니다 ", "datetime": "1", "product_id": "2022-09-01 21:50:32.380704+09:00"}}, {"model": "base.blacklist", "pk": 3, "fields": {"score": 34, "review": "벌써 새벽 4시가 다되가요", "datetime": "09020356", "product_id": "23"}}]
//     var blacklistLen=2;
//     useEffect(()=>{
//     const getApis = async () =>{
//         await axios.get("/black_list")
//         .then(
//             (response)=>{
//                 // console.log(response.data)
//                 blacklist =  response.data
//                 blacklistLen = blacklist.length            <th scope="row">{{ board.id}}</th>
//                 console.log(blacklist)
//                 //console.log(blacklist[0]['fields'])
//                 console.log(blacklistLen)
//             }
//         )}

//         getApis();
//     })

//     const _sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));

//     const timer = async () => {
//         await _sleep(1000);
//         console.log('First');
//         await _sleep(1000);
//         console.log('Second');
//     };

//     timer();

//     return (
//         <div>
//             <h1>Blacklist</h1>
//                 { blacklistLen ? 
//                         (
//                         <Table striped bordered hover responsive className='table-sm'>
//                             <thead>
//                                 <tr>
//                                     <th>product_id</th>
//                                     <th>review</th>
//                                     <th>datetime</th>
//                                     <th>score</th>
//                                 </tr>
//                             </thead>

//                             <tbody>
//                                 {blacklist}
//                                 {blacklist?.map((item) => {
//                                     return (
//                                         <tr key = {item.fields.product_id}>
//                                             <td>{item.fields.product_id}</td>
//                                             <td>{item.fields.review}</td>
//                                             <td>{item.fields.datetime}</td>
//                                             <td>{item.fields.score}</td> 
//                                         </tr>
//                                     );
//                                 })}
//                             </tbody>
//                         </Table>
//                     )
//                     : (<Message variant='danger'> There is no blacklist. </Message>)
//                 }
//         </div>
//     )
// }

// export default BlackListScreen
