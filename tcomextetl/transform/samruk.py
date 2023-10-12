from attrs import define, field


@define
class SamrukSupplierRow:
    id = field(default='')
    identifier = field(default='')
    name_kk = field(default='')
    name_ru = field(default='')
    country_id = field(default='')
    begin_date = field(default='')
    position_kk = field(default='')
    position_ru = field(default='')
    site = field(default='')
    building = field(default='')
    city = field(default='')
    flat = field(default='')
    postcode = field(default='')
    street = field(default='')
    kato_id = field(default='')
    register_type = field(default='')
    end_date = field(default='')
    bad_supplier_date = field(default='')
    include_nomenclature_date = field(default='')
    create_date = field(default='')
    last_modified_date = field(default='')


@define
class SamrukPurchaseRow:
    id = field(default='')
    row_number = field(default='')
    plan_id = field(default='')
    plan_item_group_id = field(default='')
    ext_id = field(default='')
    lot_id = field(default='')
    advert_id = field(default='')
    count_lot = field(default='')
    price_lot = field(default='')
    sum_tru_no_nds = field(default='')
    acceptance_begin_date_time = field(default='')
    acceptance_end_date_time = field(default='')
    discussion_publish_date = field(default='')
    review_publish_date = field(default='')
    admission_publish_date = field(default='')
    negotiations_publish_date = field(default='')
    summary_publish_date = field(default='')
    name_ru = field(default='')
    tender_priority = field(default='')
    jhi_comment = field(default='')
    status = field(default='')
    advert_status = field(default='')
    status_date_time = field(default='')
    zks_name = field(default='')
    supplier_name = field(default='')
    create_date = field(default='')
    last_modified_date = field(default='')


@define
class SamrukKztContractRow:
    id = field(default='')
    created_date = field(default='')
    contract_date_time = field(default='')
    contract_number = field(default='')
    control_date_time = field(default='')
    foreign_sum = field(default='')
    sum_nds = field(default='')
    sum_no_nds = field(default='')
    tender_type = field(default='')
    currency_id = field(default='')
    advert_id = field(default='')
    flag_paper_contract = field(default='')
    nds_size_id = field(default='')
    contract_items_name_kk = field(default='')
    contract_items_name_ru = field(default='')
    local_content_projected_share = field(default='')
    contract_type = field(default='')
    prev_contract_card_id = field(default='')
    main_contract_card_id = field(default='')
    system_number = field(default='')
    last_contract_card_id = field(default='')
    rescission_date_time = field(default='')
    rescission_type = field(default='')
    currency_rate_id = field(default='')
    currency_date = field(default='')
    flag_nds_lot = field(default='')
    jhi_comment = field(default='')
    status = field(default='')
    id_supplier = field(default='')
    id_customer = field(default='')
    contract_end_date_time = field(default='')
    last_modified_date = field(default='')


@define
class SamrukBadSupplierRow:
    id = field(default='')
    name_kk = field(default='')
    name_ru = field(default='')
    legal_address = field(default='')
    reason_id = field(default='')
    bad_supplier_date = field(default='')
    founder_info = field(default='')
    bin_iin = field(default='')
    begin_date = field(default='')
    end_date = field(default='')
    create_date = field(default='')
    last_modified_date = field(default='')


@define
class SamrukPlanRow:
    id = field(default='')
    identifier = field(default='')
    year = field(default='')
    type = field(default='')
    durationtype = field(default='')
    item_count = field(default='')
    status = field(default='')
    approved_plan_sum = field(default='')
    create_date = field(default='')
    last_modified_date = field(default='')


# Empty api
@define
class SamrukContractItemsRow:
    id = field(default='')
    count = field(default='')
    execution_sum_nds = field(default='')
    execution_sum_no_nds = field(default='')
    foreign_price = field(default='')
    foreign_sum = field(default='')
    sum_nds = field(default='')
    sum_no_nds = field(default='')
    contract_card_id = field(default='')
    lot_id = field(default='')
    plan_item_id = field(default='')
    price = field(default='')
    country_id = field(default='')
    prev_contract_item_id = field(default='')
    delivery_date_time = field(default='')
    final_payment = field(default='')
    interim_payment = field(default='')
    prepayment = field(default='')
    detail_ru = field(default='')
    nds_size_id = field(default='')
    local_content = field(default='')
    execution_count = field(default='')
    stkz_certificate_position_id = field(default='')
    local_content_projected_share = field(default='')
    foreign_execution_sum = field(default='')
    jhi_comment = field(default='')
    status = field(default='')
    year_count = field(default='')
    foreign_price_year = field(default='')
    foreign_sum_year = field(default='')
    price_year = field(default='')
    jhi_year = field(default='')
    sum_nds_year = field(default='')
    sum_no_nds_year = field(default='')


@define
class SamrukContractItemDeliveries:
    # couldn't retrieve correct structure
    contract_item_id = field(default='')

@define
class SamrukPlanItemRow:
    id = field(default='')
    deliveryLocation = field(default='')
    durationMonth = field(default='')
    organizerBin = field(default='')
    rowNumber = field(default='')
    singleSourceReason = field(default='')
    tenderLocation = field(default='')
    tenderPriority = field(default='')
    tenderType = field(default='')
    tenderSubjectType = field(default='')
    truCode = field(default='')
    price = field(default='')
    count = field(default='')
    sumTruNoNds = field(default='')
    sumTruNds = field(default='')
    localContent = field(default='')
    schedule_id = field(default='')
    schedule_period = field(default='')
    schedule_dayType = field(default='')
    schedule_count = field(default='')
    schedule_monthFrom = field(default='')
    schedule_monthTo = field(default='')
    schedule_flagDeliveryRequestCustomer = field(default='')
    schedule_daysForDelivery = field(default='')
    schedule_deliveryDaysType = field(default='')
    transientTender = field(default='')
    add_attribute_ru = field(default='')
    add_attribute_kz = field(default='')
    deliveryCountryCode_id = field(default='')
    deliveryCountryCode_code = field(default='')
    deliveryCountryCode_ru = field(default='')
    deliveryCountryCode_kk = field(default='')
    deliveryCountryCode_en = field(default='')
    deliveryCountryCode_rank = field(default='')
    deliveryCountryCode_finalEntry = field(default='')
    deliveryCountryCode_dictionary = field(default='')
    deliveryKatoCode_id = field(default='')
    deliveryKatoCode_code = field(default='')
    deliveryKatoCode_ru = field(default='')
    deliveryKatoCode_kk = field(default='')
    deliveryKatoCode_fullRu = field(default='')
    deliveryKatoCode_fullKk = field(default='')
    deliveryKatoCode_fullEn = field(default='')
    incotermsConditionCode_id = field(default='')
    incotermsConditionCode_code = field(default='')
    incotermsConditionCode_ru = field(default='')
    incotermsConditionCode_kk = field(default='')
    incotermsConditionCode_en = field(default='')
    incotermsConditionCode_rank = field(default='')
    incotermsConditionCode_finalEntry = field(default='')
    incotermsConditionCode_dictionary = field(default='')
    extid = field(default='')
    katoCode_id = field(default='')
    katoCode_code = field(default='')
    katoCode_ru = field(default='')
    katoCode_kk = field(default='')
    katoCode_fullRu = field(default='')
    katoCode_fullKk = field(default='')
    katoCode_fullEn = field(default='')
    mkeiCode_id = field(default='')
    mkeiCode_code = field(default='')
    mkeiCode_ru = field(default='')
    mkeiCode_kk = field(default='')
    mkeiCode_en = field(default='')
    mkeiCode_rank = field(default='')
    mkeiCode_finalEntry = field(default='')
    mkeiCode_dictionary = field(default='')
    nds_size_id = field(default='')
    noNds = field(default='')
    plan = field(default='')
    subdivision_id = field(default='')
    contract_item_id = field(default='')
    contract_id = field(default='')
    lot_id = field(default='')
    advert_id = field(default='')
    create_date = field(default='')
    last_modified_date = field(default='')


# Not in list
@define
class SamrukCertRow:
    id = field(default='')
    bin = field(default='')
    certificate_id = field(default='')
    description_kk = field(default='')
    description_ru = field(default='')
    director_name_kk = field(default='')
    director_name_ru = field(default='')
    expiration_date = field(default='')
    issue_date = field(default='')
    kato_code = field(default='')
    modified_date = field(default='')
    name_kk = field(default='')
    name_ru = field(default='')
    jhi_number = field(default='')
    organization_code = field(default='')
    series = field(default='')
    id_stkz_certificate_position = field(default='')
    box_type = field(default='')
    count = field(default='')
    percent = field(default='')
    tnved = field(default='')
    unit_code = field(default='')
    description_kk_stkz_certificate_position = field(default='')
    description_ru_stkz_certificate_position = field(default='')

# Empty api
@define
class SamrukDictRow:
    id = field(default='')
    created_date = field(default='')
    code = field(default='')
    en = field(default='')
    ru = field(default='')
    kk = field(default='')
    version = field(default='')


@define
class SamrukParticipationLotRow:
    id = field(default='')
    status = field(default='')
    lot_id = field(default='')
    status_date_time = field(default='')
    bin_iin = field(default='')
    price = field(default='')
    create_date = field(default='')
    last_modified_date = field(default='')


@define
class SamrukEntriesRow:
    id = field(default='')
    deleted = field(default='')
    code = field(default='')
    kk = field(default='')
    ru = field(default='')
    en = field(default='')
    dictionary_id = field(default='')
    parent_entry_id = field(default='')
    final_entry = field(default='')
    measure_unit_id = field(default='')
    rank = field(default='')
