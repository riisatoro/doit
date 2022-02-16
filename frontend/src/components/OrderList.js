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

    return (
        <div>
            <div className='py-3'>
                <h3 className='border-bottom'>Pin board</h3>
                {ordersData?.pinned?.map(
                    (order, index) => <OrderItem key={`${index}_${order.title}`} {...{...order, index, pinned: true, fetchAllOrders}} />)} 
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
