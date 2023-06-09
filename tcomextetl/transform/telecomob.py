from attrs import define, field


@define
class TelecomobClickLogRow:
    application_id = field(default='')
    click_datetime = field(default='')
    click_id = field(default='')
    click_ipv6 = field(default='')
    click_timestamp = field(default='')
    click_url_parameters = field(default='')
    click_user_agent = field(default='')
    publisher_id = field(default='')
    publisher_name = field(default='')
    tracker_name = field(default='')
    tracking_id = field(default='')
    city = field(default='')
    country_iso_code = field(default='')
    device_type = field(default='')
    device_model = field(default='')
    device_manufacturer = field(default='')
    os_version = field(default='')
    os_name = field(default='')
    windows_aid = field(default='')
    google_aid = field(default='')
    ios_ifv = field(default='')
    ios_ifa = field(default='')


@define
class TelecomobPostbackLogRow:
    application_id = field(default='')
    click_datetime = field(default='')
    click_id = field(default='')
    click_ipv6 = field(default='')
    click_timestamp = field(default='')
    click_url_parameters = field(default='')
    click_user_agent = field(default='')
    publisher_id = field(default='')
    publisher_name = field(default='')
    tracker_name = field(default='')
    tracking_id = field(default='')
    install_datetime = field(default='')
    install_ipv6 = field(default='')
    install_timestamp = field(default='')
    match_type = field(default='')
    appmetrica_device_id = field(default='')
    device_locale = field(default='')
    device_manufacturer = field(default='')
    device_model = field(default='')
    device_type = field(default='')
    google_aid = field(default='')
    ios_ifa = field(default='')
    ios_ifv = field(default='')
    os_name = field(default='')
    os_version = field(default='')
    windows_aid = field(default='')
    app_package_name = field(default='')
    app_version_name = field(default='')
    conversion_datetime = field(default='')
    conversion_timestamp = field(default='')
    event_name = field(default='')
    attempt_datetime = field(default='')
    attempt_timestamp = field(default='')
    cost_model = field(default='')
    notifying_status = field(default='')
    postback_url = field(default='')
    postback_url_parameters = field(default='')
    response_body = field(default='')
    response_code = field(default='')


@define
class TelecomobInstallationLogRow:
    application_id = field(default='')
    click_datetime = field(default='')
    click_id = field(default='')
    click_ipv6 = field(default='')
    click_timestamp = field(default='')
    click_url_parameters = field(default='')
    click_user_agent = field(default='')
    profile_id = field(default='')
    publisher_id = field(default='')
    publisher_name = field(default='')
    tracker_name = field(default='')
    tracking_id = field(default='')
    install_datetime = field(default='')
    install_ipv6 = field(default='')
    install_receive_datetime = field(default='')
    install_receive_timestamp = field(default='')
    install_timestamp = field(default='')
    is_reattribution = field(default='')
    is_reinstallation = field(default='')
    match_type = field(default='')
    appmetrica_device_id = field(default='')
    city = field(default='')
    connection_type = field(default='')
    country_iso_code = field(default='')
    device_locale = field(default='')
    device_manufacturer = field(default='')
    device_model = field(default='')
    device_type = field(default='')
    google_aid = field(default='')
    ios_ifa = field(default='')
    ios_ifv = field(default='')
    mcc = field(default='')
    mnc = field(default='')
    operator_name = field(default='')
    os_name = field(default='')
    os_version = field(default='')
    windows_aid = field(default='')
    app_package_name = field(default='')
    app_version_name = field(default='')


@define
class TelecomobInstallationRepRow:
    date = field(default='')
    cnt = field(default='')

@define
class TelecomobRepAcquisitionsRow:
    date = field(default='')
    os = field(default='')
    install_count = field(default='')


@define
class TelecomobRepDauRow:
    date = field(default='')
    active_users_count = field(default='')
    active_users_share = field(default='')
    new_users_count = field(default='')
    new_users_share = field(default='')


@define
class TelecomobRepDauRow:
    date = field(default='')
    active_users_count = field(default='')
    active_users_share = field(default='')
    new_users_count = field(default='')
    new_users_share = field(default='')


@define
class TelecomobRepDauRow:
    date = field(default='')
    active_users_count = field(default='')
    active_users_share = field(default='')
    new_users_count = field(default='')
    new_users_share = field(default='')