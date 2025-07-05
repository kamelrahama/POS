/** @odoo-module **/

import { Component } from "@odoo/owl";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { OrderWidget } from "@point_of_sale/app/generic_components/order_widget/order_widget";
import { omit } from "@web/core/utils/objects";


export class KitchenReceipt extends Component {
    static template = "pos_kitchen_receipt.KitchenReceipt";
    static components = {
        Orderline,
//        OrderWidget,
    };
    static props = {
        data: Object,
        formatCurrency: Function,
    };
    get itemInfo(){
        return this.props.data.orderlines;
    }
    get tableNumber(){
        return this.props.data.headerData.table
    }
    omit(...args) {
        return omit(...args);
    }
}
