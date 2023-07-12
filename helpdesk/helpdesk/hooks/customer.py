import frappe
from erpnext.selling.doctype.customer.customer import Customer
from frappe.model.document import Document

from helpdesk.helpdesk.utils.hd_customer import create_hd_customer_from_customer

logger = frappe.logger("customer", allow_site=True)

def on_customer_create(doc, method):
    create_hd_customer_from_customer(doc)
