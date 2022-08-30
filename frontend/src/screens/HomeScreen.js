import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Row, Col } from 'react-bootstrap'
import Product from '../components/Product'
import Loader from '../components/Loader'
import Message from '../components/Message'
import Paginate from '../components/Paginate'
import ProductCarousel from '../components/ProductCarousel'
import { listProducts } from '../actions/productActions'
import Tooltip from 'react-bootstrap'
import {arrow_box, tippy} from './message.css'
import style from './style.js'

function HomeScreen({ history }) {
    const dispatch = useDispatch()
    const productList = useSelector(state => state.productList)
    const { error, loading, products, page, pages } = productList
    const Ad = () => {
        const [isHovering, setIsHovering] = useState(0);}
        
            const [isHovering, setIsHovering] = useState(false);
          
            const handleMouseOver = () => {
              setIsHovering(true);
            };
          
            const handleMouseOut = () => {
              setIsHovering(false);
            };
    let keyword = history.location.search
    const [hover, setHover] = useState(false);
    useEffect(() => {
        dispatch(listProducts(keyword))

    }, [dispatch, keyword])

    return (
        <div>
            {!keyword && <ProductCarousel />}

            <h1>제품 목록</h1>
            {loading ? <Loader />
                : error ? <Message variant='danger'>{error}</Message>
                    :
                    <div>
                        <Row>
                            {products.map(product => {
                                return (
                            
                                
                                    <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
                                      
                                      <div onMouseOver={handleMouseOver} onMouseOut={handleMouseOut}>    
                                        <Product product={product} />
                                        {isHovering && product.name }</div>
                                    </Col>
                                    
                                )
                            })}
                        </Row>
                        <Paginate page={page} pages={pages} keyword={keyword} />
                    </div>
            }
        </div>
    )
}

export default HomeScreen
