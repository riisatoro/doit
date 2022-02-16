import React, { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import { PIN_ORDER_URL, UNPIN_ORDER_URL } from '../constants/urls';


const OrderItem = ({fetchAllOrders, index, slug, title, rating, description, pinned}) => {
    const { apiInstance } = useContext(AuthContext);
    const pinOrder = () => {
        if (pinned) {
            apiInstance.post(UNPIN_ORDER_URL(slug)).then(fetchAllOrders);
        } else {
            apiInstance.post(PIN_ORDER_URL(slug)).then(fetchAllOrders);
        }
    }

    return (
        <div>
            <div className='d-flex justify-content-between'>
                <div className='d-flex'>
                    <h5>{title}</h5>
                    {
                    pinned ? 
                    <i className="mx-1 btn btn-primary fa-solid fa-circle-minus" onClick={pinOrder}></i>
                    : <i className="mx-1 btn btn-primary fa-solid fa-thumbtack" onClick={pinOrder}></i>
                    }
                </div>
                <p>+ {rating} rating</p>
            </div>
            <p>{description}</p>
            <hr />
        </div>
    );
}

export default OrderItem;
