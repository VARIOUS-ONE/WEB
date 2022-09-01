// import React, { useState, useEffect } from 'react'
// import { LinkContainer } from 'react-router-bootstrap'
// import { Table, Button } from 'react-bootstrap'
// import { useDispatch, useSelector } from 'react-redux'
// import Loader from '../components/Loader'
// import Message from '../components/Message'
// import { listUsers, deleteUser } from '../actions/blackActions'

// function BlackListScreen({ history }) {

//     const dispatch = useDispatch()

//     const blackList = useSelector(state => state.blackList)
//     const { loading, error,  } = blackList


//     const userLogin = useSelector(state => state.userLogin)
//     const { userInfo } = userLogin

//     const userDelete = useSelector(state => state.userDelete)
//     const { success: successDelete } = userDelete


//     useEffect(() => {
//         if (userInfo && userInfo.isAdmin) {
//             dispatch(listUsers())
//         } else {
//             history.push('/login')
//         }

//     }, [dispatch, history, successDelete, userInfo])



//     return (
//         <div>
//             <h1>Blacklist</h1>
//             {loading
//                 ? (<Loader />)
//                 : error
//                     ? (<Message variant='danger'>{error}</Message>)
//                     : (
//                         <Table striped bordered hover responsive className='table-sm'>
//                             <thead>
//                                 <tr>
//                                     {/* <th>id</th> */}
//                                     <th>product_id</th>
//                                     <th>review</th>
//                                     <th>datetime</th>
//                                     <th>score</th>
//                                 </tr>
//                             </thead>

//                             <tbody>
//                                 {blackList.blackLists.map((Blacklist) => {
//                                     return (
//                                         <tr>
//                                         <td>{item.score}</td>
//                                         <td>{item.review}</td>
//                                         <td>{item.datetime}</td>
//                                         <td>{item.product_id}</td> 
//                                         </tr>
//                                     );
//                                 })}
                            
//                             </tbody>
//                         </Table>
//                     )}
//         </div>
//     )
// }

// export default BlackListScreen
