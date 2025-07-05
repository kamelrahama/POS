/** @odoo-module **/

import { KitchenReceipt } from "./kitchen_receipt";
import { BillScreen } from "@pos_restaurant/app/bill_screen/bill_screen";
import { ReceiptScreen } from "@point_of_sale/app/screens/receipt_screen/receipt_screen";
import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen/receipt/order_receipt";
import { registry } from "@web/core/registry";

export class KitchenReceiptScreen extends BillScreen {
    static template = "pos_kitchen_receipt.KitchenReceiptScreen";
    static components = { KitchenReceipt};
    confirm() {
        if (!this.env.isMobile) {
            this.props.resolve({ confirmed: true, payload: null });
            this.pos.closeTempScreen();
        }
    }
    /**
     * @override
     */
    async printReceipt() {
        var result = await this.printer.print(
            KitchenReceipt,
            {
                data: this.pos.get_order().export_for_printing(),
                formatCurrency: this.env.utils.formatCurrency,
            },
            { webPrintFallback: true }
        );
        this.currentOrder._printed = false;
    }

    get isBill() {
        return true;
    }
}

registry.category("pos_screens").add("KitchenReceiptScreen", KitchenReceiptScreen);