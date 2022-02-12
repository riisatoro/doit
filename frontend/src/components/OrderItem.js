import React from 'react';

const OrderItem = ({index, title, rating, description}) => {
    return (
        <div>
            <div className='d-flex justify-content-between'>
                <div className='d-flex'>
                    <h5>{title}</h5>
                    <i className="mx-1 btn btn-primary fa-solid fa-thumbtack"></i>
                </div>
                <p>+ {rating} rating</p>
            </div>
            <p>{description}</p>
            <hr />
        </div>
    );
}

export default OrderItem;
