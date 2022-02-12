import React from "react";
import { Link } from 'react-router-dom';
import OrderList from "./OrderList";
import PinnedOrders from './PinnedOrders';

function Main() {

    return (
        <div>
            <PinnedOrders />
            <OrderList />
        </div>
    )

}

export default Main;
