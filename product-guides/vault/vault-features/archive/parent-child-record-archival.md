# Parent-Child Record Archival

### **Overview** <a href="#id-1.-overview" id="id-1.-overview"></a>

AutoRABIT Vault ensures data integrity when archiving records in Salesforce by automatically including certain child records based on specific relationship criteria. This FAQ explains the scenarios where child records are considered mandatory for archival.

### Parent-Child Record Archival <a href="#q6-why-is-it-important-to-archive-both-parent-and-child-records-together" id="q6-why-is-it-important-to-archive-both-parent-and-child-records-together"></a>

It is important to archive both parent and child records together. This ensures that:

* No orphaned records are left behind.
* Data integrity is maintained.
* Salesforce restrictions and relationships remain consistent.
* Compliance and audit requirements are met.

### **Mandatory Child Record Archival Criteria** <a href="#q9-how-does-autorabit-vault-ensure-that-all-mandatory-child-records-are-archived" id="q9-how-does-autorabit-vault-ensure-that-all-mandatory-child-records-are-archived"></a>

AutoRABIT Vault analyzes Salesforce relationship configurations and automatically considers a child record mandatory for archival if it meets any of the following criteria:

* It has a **Master-Detail Relationship** with the parent.
* It is linked through a **Required Lookup Relationship** enforcing dependency.
* It is configured for **Cascade Delete,** meaning it is deleted when the parent is deleted.
* The parent deletion is prevented due to a **Restrict Parent Deletion** rule. The parent record cannot be deleted unless the child is removed, necessitating their joint archival.

This process ensures a seamless and compliant archival strategy.

### **Master-Detail Relationships** <a href="#q2-how-does-a-master-detail-relationship-affect-archival" id="q2-how-does-a-master-detail-relationship-affect-archival"></a>

A Master-Detail Relationship means that child records are inherently dependent on the parent. When a parent record is archived, all related child records must also be archived. Example: Invoice & Invoice Line Items – When an Invoice is archived, all related Invoice Line Items are archived automatically.

### **Required Lookup Relationships** <a href="#q3-what-happens-in-a-lookup-relationship-where-the-field-is-required" id="q3-what-happens-in-a-lookup-relationship-where-the-field-is-required"></a>

In Salesforce, a **Lookup Relationship** typically allows a child record to exist independently. However, if the lookup field is marked as **required**, the child record must always have a parent, mimicking a Master-Detail Relationship. When the parent is archived, the child is also archived to maintain data integrity. This is commonly found in custom objects where the lookup field is set as required, ensuring that every child record is always linked to a parent record.

### **Cascade Delete** <a href="#q4-what-is-cascade-delete-and-how-does-it-impact-archival" id="q4-what-is-cascade-delete-and-how-does-it-impact-archival"></a>

**Cascade Delete** is a Salesforce setting where deleting a parent record automatically deletes all associated child records. AutoRABIT Vault ensures these child records are archived along with the parent instead of being deleted. For example, Account & Contacts – If an Account is archived, all related Contacts are archived to maintain consistency.

### **Parent-Child Restrict Deletion** <a href="#q5-what-does-it-mean-when-a-parent-record-is-restricted-from-deletion-due-to-a-child-record" id="q5-what-does-it-mean-when-a-parent-record-is-restricted-from-deletion-due-to-a-child-record"></a>

Salesforce enforces a rule preventing a parent record from being deleted if it has associated child records. If a parent record with a restrict deletion rule is archived without its associated child, Salesforce enforces the restriction, meaning the archival process would fail unless the child records are also archived. AutoRABIT Vault ensures these relationships are accounted for automatically.

When archiving such a parent record, the child must also be archived to comply with Salesforce restrictions; otherwise, the archival will fail. For example: Contacts and Cases – A Contact cannot be deleted if it has associated cases. Archiving the Contact requires archiving its related Cases as well.

### **Configuring a Lookup Relationship Like a Master-Detail Relationship** <a href="#q7-can-a-lookup-relationship-be-configured-to-act-like-a-master-detail-relationship" id="q7-can-a-lookup-relationship-be-configured-to-act-like-a-master-detail-relationship"></a>

By marking the lookup field as **required**, you can enforce a dependency similar to a Master-Detail Relationship. This ensures that the child always references a valid parent, making its archival necessary when the parent is archived.

### Email Messages Relationships

Email messages are mandatory child records for objects to which the email messages hold a direct relationship. Email messages will hold direct relationship to the following objects through the fields ‘RelatedToId’ and the ‘ParentId’:

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">Account<br>Accreditation<br>AssessmentIndicatorDefinition<br>AssessmentTask<br>AssessmentTaskContentDocument<br>AssessmentTaskDefinition<br>AssessmentTaskOrder<br>Asset<br>AssetRelationship<br>AssignedResource<br>Award<br>BoardCertification<br>BusinessLicense<br>BusinessMilestone<br>BusinessProfile<br>Campaign<br>CareBarrier<br>CareBarrierDeterminant<br>CareBarrierType<br>CareDeterminant<br>CareDeterminantType<br>CareDiagnosis<br>CareInterventionType<br>CareMetricTarget<br>CareObservation<br>CareObservationComponent<br>CarePgmProvHealthcareProvider<br>CarePreauth<br>CarePreauthItem<br>CareProgram<br>CareProgramCampaign<br>CareProgramEligibilityRule<br>CareProgramEnrollee<br>CareProgramEnrolleeProduct<br>CareProgramEnrollmentCard<br>CareProgramGoal</td><td valign="top">CareProgramProduct<br>CareProgramProvider<br>CareProgramTeamMember<br>CareProviderAdverseAction<br>CareProviderFacilitySpecialty<br>CareProviderSearchableField<br>CareRegisteredDevice<br>CareRequest<br>CareRequestDrug<br>CareRequestExtension<br>CareRequestItem<br>CareSpecialty<br>CareSpecialtyTaxonomy<br>CareTaxonomy<br>Case<br>CommSubscriptionConsent<br>ContactEncounter<br>ContactEncounterParticipant<br>ContactRequest<br>Contract<br>CoverageBenefit<br>CoverageBenefitItem<br>CreditMemo<br>DelegatedAccount<br>DocumentChecklistItem<br>EnrollmentEligibilityCriteria<br>HealthcareFacility<br>HealthcareFacilityNetwork<br>HealthcarePayerNetwork<br>HealthcarePractitionerFacility<br>HealthcareProvider<br>HealthcareProviderNpi<br>HealthcareProviderSpecialty<br>HealthcareProviderTaxonomy<br>IdentityDocument</td><td valign="top"><p>Image<br>IndividualApplication<br>Invoice<br>ListEmail<br>Location<br>MemberPlan<br>Opportunity<br>Order<br>OtherComponentTask<br>PartyConsent<br>PersonLifeEvent<br>PlanBenefit<br>PlanBenefitItem<br>ProcessException<br>Product2<br>ProductItem<br>ProductRequest<br>ProductRequestLineItem<br>ProductTransfer<br>PurchaserPlan<br>ReceivedDocument<br>ResourceAbsence<br>ReturnOrder<br>ReturnOrderLineItem<br>ServiceAppointment<br>ServiceResource<br>Shift<br>Shipment<br>ShipmentItem<br>Solution<br>Visit<br>VisitedParty<br>VolunteerProject<br>WorkOrder<br>WorkOrderLineItem</p><p> </p></td></tr></tbody></table>

If an object has a reference from another object as both parent and child, then the parent will only be considered for a backup but not for archival. The child records will only be considered for archival.&#x20;

For more information, refer to this [Salesforce Developer](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_emailmessage.htm) resource.
