import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../context/AuthContext';
import { ORDERS_URL } from '../constants/urls';
import OrderItem from './OrderItem';
import _ from 'lodash';

const OrderList = () => {
    const [ordersData, setOrdersData] = useState({});
    const { apiInstance, isAuthenticated } = useContext(AuthContext);

    const fetchAllOrders = _.throttle(() => {
        apiInstance.get(ORDERS_URL()).then(({ data }) => {
            setOrdersData(data);
        });
    }, 2 * 1000);

    useEffect(() => {
        if (isAuthenticated) fetchAllOrders();
    }, 
    [isAuthenticated]);

    console.log(ordersData.pinned)

    return (
        <div>
            <div className='py-3'>
                <h3 className='border-bottom'>Pin board</h3>
                {ordersData?.pinned?.map(
                    (application, index) => <OrderItem key={`${index}_${application.order.title}`} {...{...application.order, index, fetchAllOrders, application, review_required: application.review_required}} />)} 
            </div>
            <div className='py-3'>
                <h3 className='border-bottom'>All tasks</h3>
                {ordersData?.list?.map(
                    (order, index) => <OrderItem key={`${index}_${order.title}`} {...{...order, index, fetchAllOrders}} />)} 
            </div>
        </div>
    )
}

export default OrderList;
