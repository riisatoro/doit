import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../context/AuthContext';
import { PINNED_ORDERS_URL } from '../constants/urls';
import OrderItem from './OrderItem';

const PinnedOrders = () => {
const [ordersData, setOrdersData] = useState({});
    const { apiInstance, isAuthenticated } = useContext(AuthContext);

    const fetchOrders = () => {
        apiInstance.get(PINNED_ORDERS_URL())
        .then(({ data }) => {
            setOrdersData(data);
        });
    }

    useEffect(() => {
        if (isAuthenticated) fetchOrders()
    }, 
    [isAuthenticated]);

    return (
        <div className='py-3'>
            <h3 className='border-bottom'>Pin board</h3>
            {ordersData?.results?.map((order, index) => <OrderItem key={`${index}_${order.title}`} {...{...order, index}} />)} 
        </div>
    )
}

export default PinnedOrders;
