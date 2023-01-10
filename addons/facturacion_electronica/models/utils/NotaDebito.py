#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xml.dom import minidom

class NotaDebito:
    def __init__(self):
        self.doc = minidom.Document()

    def Root(self):
        root = self.doc.createElement('DebitNote')
        self.doc.appendChild(root)
        root.setAttribute('xmlns', 'urn:oasis:names:specification:ubl:schema:xsd:DebitNote-2')
        root.setAttribute('xmlns:cac', 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2')
        root.setAttribute('xmlns:cbc', 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2')
        root.setAttribute('xmlns:ccts', 'urn:un:unece:uncefact:documentation:2')
        root.setAttribute('xmlns:ds', 'http://www.w3.org/2000/09/xmldsig#')
        root.setAttribute('xmlns:ext', 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2')
        root.setAttribute('xmlns:qdt', 'urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2')
        root.setAttribute('xmlns:sac', 'urn:sunat:names:specification:ubl:peru:schema:xsd:SunatAggregateComponents-1')
        root.setAttribute('xmlns:udt', 'urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2')
        root.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        
        return root

    def UBLExtensions(self):
        extUBLExtensions = self.doc.createElement('ext:UBLExtensions')
        extUBLExtensions.appendChild(self.firma(id="placeholder"))

        return extUBLExtensions
    
    def firma(self,id):
        UBLExtension=self.doc.createElement("ext:UBLExtension")
        ExtensionContent=self.doc.createElement("ext:ExtensionContent")
        Signature=self.doc.createElement("ds:Signature")
        Signature.setAttribute("Id",id)
        ExtensionContent.appendChild(Signature)
        UBLExtension.appendChild(ExtensionContent)

        return UBLExtension

    def UBLVersion(self,id):
        UBLVersion = self.doc.createElement('cbc:UBLVersionID')
        text = self.doc.createTextNode(id)
        UBLVersion.appendChild(text)

        return UBLVersion

    def CustomizationID(self,id):
        cbcCustomizationID = self.doc.createElement('cbc:CustomizationID')
        text = self.doc.createTextNode(str(id))
        cbcCustomizationID.appendChild(text)

        return cbcCustomizationID
    
    def ID(self,id):
        cbcID = self.doc.createElement('cbc:ID')
        text = self.doc.createTextNode(id)
        cbcID.appendChild(text)

        return cbcID

    def issueDate(self,fecha):
        cbcIssueDate = self.doc.createElement('cbc:IssueDate')
        text = self.doc.createTextNode(str(fecha))
        cbcIssueDate.appendChild(text)

        return cbcIssueDate

    def documentCurrencyCode(self,documentcurrencycode):
        cbcDocumentCurrencyCode = self.doc.createElement('cbc:DocumentCurrencyCode')
        text = self.doc.createTextNode(documentcurrencycode)
        cbcDocumentCurrencyCode.appendChild(text)

        return cbcDocumentCurrencyCode

    def DiscrepancyResponse(self, reference_id, response_code, description):
        DiscrepancyResponse = self.doc.createElement('cac:DiscrepancyResponse')

        ReferenceId = self.doc.createElement('cbc:ReferenceID')
        text = self.doc.createTextNode(reference_id)
        ReferenceId.appendChild(text)
        
        ResponseCode = self.doc.createElement('cbc:ResponseCode')
        text = self.doc.createTextNode(response_code)
        ResponseCode.appendChild(text)
        
        Description = self.doc.createElement('cbc:Description')
        text = self.doc.createTextNode(description)
        Description.appendChild(text)
        
        DiscrepancyResponse.appendChild(ReferenceId)
        DiscrepancyResponse.appendChild(ResponseCode)
        DiscrepancyResponse.appendChild(Description)

        return DiscrepancyResponse

    def BillingReference(self, invoice_id, invoice_type_code):
        BillingReference = self.doc.createElement('cac:BillingReference')
        InvoiceDocumentReference = self.doc.createElement('cac:InvoiceDocumentReference')

        InvoiceId = self.doc.createElement('cbc:ID')
        text = self.doc.createTextNode(invoice_id)
        InvoiceId.appendChild(text)
            
        InvoiceDocumentReference.appendChild(InvoiceId)

        BillingReference.appendChild(InvoiceDocumentReference)
        
        return BillingReference

    def NotaDebitoRoot(self, rootXML, versionid, customizationid, id, issue_date, documentcurrencycode):
        NotaDebitoRoot = rootXML
        NotaDebitoRoot.appendChild(self.UBLVersion(versionid))
        NotaDebitoRoot.appendChild(self.CustomizationID(customizationid))
        NotaDebitoRoot.appendChild(self.ID(id))
        NotaDebitoRoot.appendChild(self.issueDate(issue_date))
        NotaDebitoRoot.appendChild(self.documentCurrencyCode(documentcurrencycode))
        return NotaDebitoRoot
    
    def Signature(self, signatureid, partyid, partyname, uri):
        Signature = self.doc.createElement('cac:Signature')

        ID = self.doc.createElement('cbc:ID')
        text = self.doc.createTextNode(signatureid)
        ID.appendChild(text)

        SignatoryParty = self.doc.createElement('cac:SignatoryParty')
        PartyIdentification = self.doc.createElement('cac:PartyIdentification')
        _ID = self.doc.createElement('cbc:ID')
        text = self.doc.createTextNode(partyid)
        _ID.appendChild(text)

        PartyName = self.doc.createElement('cac:PartyName')
        Name = self.doc.createElement('cbc:Name')
        text = self.doc.createTextNode(partyname)
        Name.appendChild(text)

        DigitalSignatureAttachment = self.doc.createElement('cac:DigitalSignatureAttachment')
        ExternalReference = self.doc.createElement('cac:ExternalReference')
        URI = self.doc.createElement('cbc:URI')
        text = self.doc.createTextNode(uri)
        URI.appendChild(text)

        PartyIdentification.appendChild(_ID)
        PartyName.appendChild(Name)

        ExternalReference.appendChild(URI)

        SignatoryParty.appendChild(PartyIdentification)
        SignatoryParty.appendChild(PartyName)

        DigitalSignatureAttachment.appendChild(ExternalReference)
            
        Signature.appendChild(ID)
        Signature.appendChild(SignatoryParty)
        Signature.appendChild(DigitalSignatureAttachment)

        return Signature

    def AccountingSupplierParty(self, registrationname, companyid):
        AccountingSupplierParty = self.doc.createElement('cac:AccountingSupplierParty')
        Party = self.doc.createElement('cac:Party')
        PartyIdentification = self.doc.createElement('cac:PartyIdentification')
        ID = self.doc.createElement('cbc:ID')
        ID.setAttribute('schemeID', '6')
        text = self.doc.createTextNode(companyid)
        ID.appendChild(text)
        
        PartyLegalEntity = self.doc.createElement('cac:PartyLegalEntity')
        RegistrationName = self.doc.createElement('cbc:RegistrationName')
        text = self.doc.createTextNode(registrationname)
        RegistrationName.appendChild(text)

        RegistrationAddress = self.doc.createElement('cac:RegistrationAddress')
        AddressTypeCode = self.doc.createElement('cbc:AddressTypeCode')
        text = self.doc.createTextNode('0000')
        AddressTypeCode.appendChild(text)

        RegistrationAddress.appendChild(AddressTypeCode)

        PartyIdentification.appendChild(ID)
        PartyLegalEntity.appendChild(RegistrationName)
        PartyLegalEntity.appendChild(RegistrationAddress)

        Party.appendChild(PartyIdentification)
        Party.appendChild(PartyLegalEntity)

        AccountingSupplierParty.appendChild(Party)

        return AccountingSupplierParty

    def AccountingCustomerParty(self, customername, customerid, customertipo):
        AccountingCustomerParty = self.doc.createElement('cac:AccountingCustomerParty')
        Party = self.doc.createElement('cac:Party')
        PartyIdentification = self.doc.createElement('cac:PartyIdentification')
        ID = self.doc.createElement('cbc:ID')
        ID.setAttribute('schemeID', str(customertipo))
        text = self.doc.createTextNode(customerid)
        ID.appendChild(text)
        
        PartyLegalEntity = self.doc.createElement('cac:PartyLegalEntity')
        RegistrationName = self.doc.createElement('cbc:RegistrationName')
        text = self.doc.createTextNode(customername)
        RegistrationName.appendChild(text)

        PartyIdentification.appendChild(ID)
        PartyLegalEntity.appendChild(RegistrationName)

        Party.appendChild(PartyIdentification)
        Party.appendChild(PartyLegalEntity)

        AccountingCustomerParty.appendChild(Party)

        return AccountingCustomerParty

    def RequestedMonetaryTotal(self, payable_amount):
        RequestedMonetaryTotal = self.doc.createElement('cac:RequestedMonetaryTotal')

        PayableAmount = self.doc.createElement('cbc:PayableAmount')
        PayableAmount.setAttribute('currencyID', 'PEN')
        text = self.doc.createTextNode(payable_amount)
        PayableAmount.appendChild(text)

        RequestedMonetaryTotal.appendChild(PayableAmount)
        return RequestedMonetaryTotal


    def DebitNoteLine(self, id, valor, unitCode, quantity, currency, price, taxtotal, afectacion):
        DebitNoteLine = self.doc.createElement('cac:DebitNoteLine')
        ID = self.doc.createElement('cbc:ID')
        text = self.doc.createTextNode(str(id))
        ID.appendChild(text)

        DebitedQuantity = self.doc.createElement('cbc:DebitedQuantity')
        DebitedQuantity.setAttribute('unitCode', str(unitCode))
        text = self.doc.createTextNode(quantity)
        DebitedQuantity.appendChild(text)

        LineExtensionAmount = self.doc.createElement('cbc:LineExtensionAmount')
        LineExtensionAmount.setAttribute('currencyID', currency)
        text = self.doc.createTextNode(str(valor))
        LineExtensionAmount.appendChild(text)

        Price = self.doc.createElement('cac:Price')
        PriceAmount = self.doc.createElement('cbc:PriceAmount')
        PriceAmount.setAttribute('currencyID', currency)
        text = self.doc.createTextNode(str(price))
        PriceAmount.appendChild(text)

        TaxTotal = self.doc.createElement('cac:TaxTotal')
        TaxAmount = self.doc.createElement('cbc:TaxAmount')
        TaxAmount.setAttribute('currencyID', currency)
        text = self.doc.createTextNode(str(taxtotal))
        TaxAmount.appendChild(text)

        TaxSubtotal = self.doc.createElement('cac:TaxSubtotal')
        TaxableAmount = self.doc.createElement('cbc:TaxableAmount')
        TaxableAmount.setAttribute('currencyID', currency)
        text = self.doc.createTextNode(valor)
        TaxableAmount.appendChild(text)
        _TaxAmount = self.doc.createElement('cbc:TaxAmount')
        _TaxAmount.setAttribute('currencyID', currency)
        text = self.doc.createTextNode(str(taxtotal))
        _TaxAmount.appendChild(text)
        TaxCategory = self.doc.createElement('cac:TaxCategory')
        Percent = self.doc.createElement('cbc:Percent')
        text = self.doc.createTextNode('18.00')
        Percent.appendChild(text)
        TaxExemptionReasonCode = self.doc.createElement('cbc:TaxExemptionReasonCode')
        text = self.doc.createTextNode(afectacion)
        TaxExemptionReasonCode.appendChild(text)
        TaxScheme = self.doc.createElement('cac:TaxScheme')
        
        if afectacion == '10':
            taxcode = '1000'
            taxname = 'IGV'
            taxtype = 'VAT'

        elif afectacion in ('11', '12', '13', '14', '15', '16', '21', '31', '32', '33', '34', '35', '36'):
            taxcode = '9996'
            taxname = 'GRA'
            taxtype = 'FRE'
        
        elif afectacion == '20':
            taxcode = '9997'
            taxname = 'EXO'
            taxtype = 'VAT'
        
        elif afectacion == '30':
            taxcode = '9998'
            taxname = 'INA'
            taxtype = 'FRE'

        _ID = self.doc.createElement('cbc:ID')
        text = self.doc.createTextNode(taxcode)
        _ID.appendChild(text)
        Name = self.doc.createElement('cbc:Name')
        text = self.doc.createTextNode(taxname)
        Name.appendChild(text)
        TaxTypeCode = self.doc.createElement('cbc:TaxTypeCode')
        text = self.doc.createTextNode(taxtype)
        TaxTypeCode.appendChild(text)

        TaxScheme.appendChild(_ID)
        TaxScheme.appendChild(Name)
        TaxScheme.appendChild(TaxTypeCode)

        TaxCategory.appendChild(Percent)
        TaxCategory.appendChild(TaxExemptionReasonCode)
        TaxCategory.appendChild(TaxScheme)

        TaxSubtotal.appendChild(TaxableAmount)
        TaxSubtotal.appendChild(_TaxAmount)
        TaxSubtotal.appendChild(TaxCategory)

        Price.appendChild(PriceAmount)
        TaxTotal.appendChild(TaxAmount)
        TaxTotal.appendChild(TaxSubtotal)

        DebitNoteLine.appendChild(ID)
        DebitNoteLine.appendChild(DebitedQuantity)
        DebitNoteLine.appendChild(LineExtensionAmount)
        DebitNoteLine.appendChild(TaxTotal)
        DebitNoteLine.appendChild(Price)
        # DebitNoteLine.appendChild(PricingReference)

        return DebitNoteLine

    # def cacTaxTotal(self, currency_id, taxtotal):
    def cacTaxTotal(self, currency_id, taxtotal, gravado, inafecto, exonerado, gratuito):
        cacTaxTotal = self.doc.createElement('cac:TaxTotal')
        cbcTaxAmount = self.doc.createElement('cbc:TaxAmount')
        cbcTaxAmount.setAttribute('currencyID', currency_id)
        text = self.doc.createTextNode(str(taxtotal))
        cbcTaxAmount.appendChild(text)

        cacTaxTotal.appendChild(cbcTaxAmount)
        
        if gravado != '0.0':
            cacTaxSubtotal = self.doc.createElement('cac:TaxSubtotal')
            cbcTaxableAmount = self.doc.createElement('cbc:TaxableAmount')
            cbcTaxableAmount.setAttribute('currencyID', currency_id)
            text = self.doc.createTextNode(gravado)
            cbcTaxableAmount.appendChild(text)

            _cbcTaxAmount = self.doc.createElement('cbc:TaxAmount')
            _cbcTaxAmount.setAttribute('currencyID', currency_id)
            text = self.doc.createTextNode(taxtotal)
            _cbcTaxAmount.appendChild(text)

            cacTaxCategory = self.doc.createElement('cac:TaxCategory')
            cacTaxScheme = self.doc.createElement('cac:TaxScheme')
            cbcID = self.doc.createElement('cbc:ID')
            text = self.doc.createTextNode('1000')
            cbcID.appendChild(text)

            cbcName = self.doc.createElement('cbc:Name')
            text = self.doc.createTextNode('IGV')
            cbcName.appendChild(text)

            cbcTaxTypeCode = self.doc.createElement('cbc:TaxTypeCode')
            text = self.doc.createTextNode('VAT')
            cbcTaxTypeCode.appendChild(text)
            
            cacTaxScheme.appendChild(cbcID)
            cacTaxScheme.appendChild(cbcName)
            cacTaxScheme.appendChild(cbcTaxTypeCode)

            cacTaxCategory.appendChild(cacTaxScheme)
                
            cacTaxSubtotal.appendChild(cbcTaxableAmount)
            cacTaxSubtotal.appendChild(_cbcTaxAmount)
            cacTaxSubtotal.appendChild(cacTaxCategory)

            cacTaxTotal.appendChild(cacTaxSubtotal)

        if inafecto != '0.0':
            cacTaxSubtotal = self.doc.createElement('cac:TaxSubtotal')
            cbcTaxableAmount = self.doc.createElement('cbc:TaxableAmount')
            cbcTaxableAmount.setAttribute('currencyID', currency_id)
            text = self.doc.createTextNode(inafecto)
            cbcTaxableAmount.appendChild(text)

            _cbcTaxAmount = self.doc.createElement('cbc:TaxAmount')
            _cbcTaxAmount.setAttribute('currencyID', currency_id)
            text = self.doc.createTextNode('0.00')
            _cbcTaxAmount.appendChild(text)

            cacTaxCategory = self.doc.createElement('cac:TaxCategory')
            cacTaxScheme = self.doc.createElement('cac:TaxScheme')
            cbcID = self.doc.createElement('cbc:ID')
            text = self.doc.createTextNode('9998')
            cbcID.appendChild(text)

            cbcName = self.doc.createElement('cbc:Name')
            text = self.doc.createTextNode('INA')
            cbcName.appendChild(text)

            cbcTaxTypeCode = self.doc.createElement('cbc:TaxTypeCode')
            text = self.doc.createTextNode('FRE')
            cbcTaxTypeCode.appendChild(text)

            cacTaxScheme.appendChild(cbcID)
            cacTaxScheme.appendChild(cbcName)
            cacTaxScheme.appendChild(cbcTaxTypeCode)

            cacTaxCategory.appendChild(cacTaxScheme)
                
            cacTaxSubtotal.appendChild(cbcTaxableAmount)
            cacTaxSubtotal.appendChild(_cbcTaxAmount)
            cacTaxSubtotal.appendChild(cacTaxCategory)
        
            cacTaxTotal.appendChild(cacTaxSubtotal)
        
        if exonerado != '0.0':
            cacTaxSubtotal = self.doc.createElement('cac:TaxSubtotal')
            cbcTaxableAmount = self.doc.createElement('cbc:TaxableAmount')
            cbcTaxableAmount.setAttribute('currencyID', currency_id)
            text = self.doc.createTextNode(exonerado)
            cbcTaxableAmount.appendChild(text)

            _cbcTaxAmount = self.doc.createElement('cbc:TaxAmount')
            _cbcTaxAmount.setAttribute('currencyID', currency_id)
            text = self.doc.createTextNode('0.00')
            _cbcTaxAmount.appendChild(text)

            cacTaxCategory = self.doc.createElement('cac:TaxCategory')
            cacTaxScheme = self.doc.createElement('cac:TaxScheme')
            cbcID = self.doc.createElement('cbc:ID')
            text = self.doc.createTextNode('9997')
            cbcID.appendChild(text)

            cbcName = self.doc.createElement('cbc:Name')
            text = self.doc.createTextNode('EXO')
            cbcName.appendChild(text)

            cbcTaxTypeCode = self.doc.createElement('cbc:TaxTypeCode')
            text = self.doc.createTextNode('VAT')
            cbcTaxTypeCode.appendChild(text)

            cacTaxScheme.appendChild(cbcID)
            cacTaxScheme.appendChild(cbcName)
            cacTaxScheme.appendChild(cbcTaxTypeCode)

            cacTaxCategory.appendChild(cacTaxScheme)
                
            cacTaxSubtotal.appendChild(cbcTaxableAmount)
            cacTaxSubtotal.appendChild(_cbcTaxAmount)
            cacTaxSubtotal.appendChild(cacTaxCategory)
        
            cacTaxTotal.appendChild(cacTaxSubtotal)

        if gratuito != '0.0':
            cacTaxSubtotal = self.doc.createElement('cac:TaxSubtotal')
            cbcTaxableAmount = self.doc.createElement('cbc:TaxableAmount')
            cbcTaxableAmount.setAttribute('currencyID', currency_id)
            text = self.doc.createTextNode(gratuito)
            cbcTaxableAmount.appendChild(text)

            _cbcTaxAmount = self.doc.createElement('cbc:TaxAmount')
            _cbcTaxAmount.setAttribute('currencyID', currency_id)
            text = self.doc.createTextNode('0.00')
            _cbcTaxAmount.appendChild(text)

            cacTaxCategory = self.doc.createElement('cac:TaxCategory')
            cacTaxScheme = self.doc.createElement('cac:TaxScheme')
            cbcID = self.doc.createElement('cbc:ID')
            text = self.doc.createTextNode('9996')
            cbcID.appendChild(text)

            cbcName = self.doc.createElement('cbc:Name')
            text = self.doc.createTextNode('GRA')
            cbcName.appendChild(text)

            cbcTaxTypeCode = self.doc.createElement('cbc:TaxTypeCode')
            text = self.doc.createTextNode('FRE')
            cbcTaxTypeCode.appendChild(text)

            cacTaxScheme.appendChild(cbcID)
            cacTaxScheme.appendChild(cbcName)
            cacTaxScheme.appendChild(cbcTaxTypeCode)

            cacTaxCategory.appendChild(cacTaxScheme)
                
            cacTaxSubtotal.appendChild(cbcTaxableAmount)
            cacTaxSubtotal.appendChild(_cbcTaxAmount)
            cacTaxSubtotal.appendChild(cacTaxCategory)
        
            cacTaxTotal.appendChild(cacTaxSubtotal)
        
        return cacTaxTotal
