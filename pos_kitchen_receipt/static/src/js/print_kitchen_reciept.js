/** @odoo-module */

import { KitchenReceiptScreen } from "./kitchen_receipt_screen";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { PrintBillButton } from "@pos_restaurant/app/control_buttons/print_bill_button/print_bill_button";


export class PrintKitchenReceipt extends PrintBillButton {
    static template = "pos_kitchen_receipt.PrintKitchenReceipt";

    async click() {
        var data = this.pos.get_order().export_for_printing();
        this.pos.showTempScreen("KitchenReceiptScreen");
    }
}

ProductScreen.addControlButton({
    component: PrintKitchenReceipt,
    condition: function () {
        return this.pos.config.iface_printbill;
    },
});