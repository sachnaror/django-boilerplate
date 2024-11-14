# Generated by Django 3.2.15 on 2024-08-12 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date_format', models.CharField(choices=[('MM/DD/YYYY', 'MM/DD/YYYY (e.g., 04/03/2024)'), ('DD.MM.YYYY', 'DD.MM.YYYY (e.g., 03.04.2024)'), ('DD/MM/YYYY', 'DD/MM/YYYY (e.g., 03/04/2024)'), ('MMM/DD/YYYY', 'MMM/DD/YYYY (e.g., Apr/03/2024)'), ('DD.MMM.YYYY', 'DD.MMM.YYYY (e.g., 03.Apr.2024)'), ('DD/MMM/YYYY', 'DD/MMM/YYYY (e.g., 03/Apr/2024)')], default='MM/DD/YYYY', max_length=20)),
                ('timezone', models.CharField(choices=[('Etc/GMT+12', '(IST-12:00) International Date Line West'), ('Etc/GMT+11', '(IST-11:00) Coordinated Universal Time-11'), ('Etc/GMT+10', '(IST-10:00) Hawaii'), ('America/Anchorage', '(IST-09:00) Alaska'), ('America/Santa_Isabel', '(IST-08:00) Baja California'), ('America/Los_Angeles', '(IST-07:00) Pacific Daylight Time (US & Canada)'), ('America/Los_Angeles', '(IST-08:00) Pacific Standard Time (US & Canada)'), ('America/Creston', '(IST-07:00) Arizona'), ('America/Chihuahua', '(IST-07:00) Chihuahua, La Paz, Mazatlan'), ('America/Boise', '(IST-07:00) Mountain Time (US & Canada)'), ('America/Belize', '(IST-06:00) Central America'), ('America/Chicago', '(IST-06:00) Central Time (US & Canada)'), ('America/Bahia_Banderas', '(IST-06:00) Guadalajara, Mexico City, Monterrey'), ('America/Regina', '(IST-06:00) Saskatchewan'), ('America/Bogota', '(IST-05:00) Bogota, Lima, Quito'), ('America/Detroit', '(IST-05:00) Eastern Time (US & Canada)'), ('America/Detroit', '(IST-04:00) Eastern Daylight Time (US & Canada)'), ('America/Indiana/Marengo', '(IST-05:00) Indiana (East)'), ('America/Caracas', '(IST-04:30) Caracas'), ('America/Asuncion', '(IST-04:00) Asuncion'), ('America/Glace_Bay', '(IST-04:00) Atlantic Time (Canada)'), ('America/Campo_Grande', '(IST-04:00) Cuiaba'), ('America/Anguilla', '(IST-04:00) Georgetown, La Paz, Manaus, San Juan'), ('America/Santiago', '(IST-04:00) Santiago'), ('America/St_Johns', '(IST-03:30) Newfoundland'), ('America/Sao_Paulo', '(IST-03:00) Brasilia'), ('America/Argentina/Buenos_Aires', '(IST-03:00) Buenos Aires'), ('America/Araguaina', '(IST-03:00) Cayenne, Fortaleza'), ('America/Godthab', '(IST-03:00) Greenland'), ('America/Montevideo', '(IST-03:00) Montevideo'), ('America/Bahia', '(IST-03:00) Salvador'), ('America/Noronha', '(IST-02:00) Coordinated Universal Time-02'), ('America/Scoresbysund', '(IST-01:00) Azores'), ('Atlantic/Cape_Verde', '(IST-01:00) Cape Verde Is.'), ('Africa/Casablanca', '(IST) Casablanca'), ('America/Danmarkshavn', '(IST) Coordinated Universal Time'), ('Europe/Isle_of_Man', '(IST) Edinburgh, London'), ('Europe/Isle_of_Man', '(IST+01:00) Edinburgh, London'), ('Atlantic/Canary', '(IST) Dublin, Lisbon'), ('Africa/Abidjan', '(IST) Monrovia, Reykjavik'), ('Arctic/Longyearbyen', '(IST+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna'), ('Europe/Belgrade', '(IST+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague'), ('Africa/Ceuta', '(IST+01:00) Brussels, Copenhagen, Madrid, Paris'), ('Europe/Sarajevo', '(IST+01:00) Sarajevo, Skopje, Warsaw, Zagreb'), ('Africa/Algiers', '(IST+01:00) West Central Africa'), ('Africa/Windhoek', '(IST+01:00) Windhoek'), ('Asia/Nicosia', '(IST+02:00) Athens, Bucharest'), ('Asia/Beirut', '(IST+02:00) Beirut'), ('Africa/Cairo', '(IST+02:00) Cairo'), ('Asia/Damascus', '(IST+02:00) Damascus'), ('Asia/Nicosia', '(IST+02:00) E. Europe'), ('Africa/Blantyre', '(IST+02:00) Harare, Pretoria'), ('Europe/Helsinki', '(IST+02:00) Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius'), ('Europe/Istanbul', '(IST+03:00) Istanbul'), ('Asia/Jerusalem', '(IST+02:00) Jerusalem'), ('Africa/Tripoli', '(IST+02:00) Tripoli'), ('Asia/Amman', '(IST+03:00) Amman'), ('Asia/Baghdad', '(IST+03:00) Baghdad'), ('Europe/Kaliningrad', '(IST+02:00) Kaliningrad'), ('Asia/Aden', '(IST+03:00) Kuwait, Riyadh'), ('Africa/Addis_Ababa', '(IST+03:00) Nairobi'), ('Europe/Kirov', '(IST+03:00) Moscow, St. Petersburg, Volgograd, Minsk'), ('Europe/Astrakhan', '(IST+04:00) Samara, Ulyanovsk, Saratov'), ('Asia/Tehran', '(IST+03:30) Tehran'), ('Asia/Dubai', '(IST+04:00) Abu Dhabi, Muscat'), ('Asia/Baku', '(IST+04:00) Baku'), ('Indian/Mahe', '(IST+04:00) Port Louis'), ('Asia/Tbilisi', '(IST+04:00) Tbilisi'), ('Asia/Yerevan', '(IST+04:00) Yerevan'), ('Asia/Kabul', '(IST+04:30) Kabul'), ('Antarctica/Mawson', '(IST+05:00) Ashgabat, Tashkent'), ('Asia/Yekaterinburg', '(IST+05:00) Yekaterinburg'), ('Asia/Karachi', '(IST+05:00) Islamabad, Karachi'), ('Asia/Kolkata', '(IST+05:30) Chennai, Kolkata, Mumbai, New Delhi'), ('Asia/Colombo', '(IST+05:30) Sri Jayawardenepura'), ('Asia/Kathmandu', '(IST+05:45) Kathmandu'), ('Antarctica/Vostok', '(IST+06:00) Nur-Sultan (Astana)'), ('Asia/Dhaka', '(IST+06:00) Dhaka'), ('Asia/Rangoon', '(IST+06:30) Yangon (Rangoon)'), ('Antarctica/Davis', '(IST+07:00) Bangkok, Hanoi, Jakarta'), ('Asia/Novokuznetsk', '(IST+07:00) Novosibirsk'), ('Asia/Hong_Kong', '(IST+08:00) Beijing, Chongqing, Hong Kong, Urumqi'), ('Asia/Krasnoyarsk', '(IST+08:00) Krasnoyarsk'), ('Asia/Brunei', '(IST+08:00) Kuala Lumpur, Singapore'), ('Antarctica/Casey', '(IST+08:00) Perth'), ('Asia/Taipei', '(IST+08:00) Taipei'), ('Asia/Choibalsan', '(IST+08:00) Ulaanbaatar'), ('Asia/Irkutsk', '(IST+08:00) Irkutsk'), ('Asia/Dili', '(IST+09:00) Osaka, Sapporo, Tokyo'), ('Asia/Pyongyang', '(IST+09:00) Seoul'), ('Australia/Adelaide', '(IST+09:30) Adelaide'), ('Australia/Darwin', '(IST+09:30) Darwin'), ('Australia/Brisbane', '(IST+10:00) Brisbane'), ('Australia/Melbourne', '(IST+10:00) Canberra, Melbourne, Sydney'), ('Antarctica/DumontDUrville', '(IST+10:00) Guam, Port Moresby'), ('Australia/Currie', '(IST+10:00) Hobart'), ('Asia/Chita', '(IST+09:00) Yakutsk'), ('Antarctica/Macquarie', '(IST+11:00) Solomon Is., New Caledonia'), ('Asia/Sakhalin', '(IST+11:00) Vladivostok'), ('Antarctica/McMurdo', '(IST+12:00) Auckland, Wellington'), ('Etc/GMT-12', '(IST+12:00) Coordinated Universal Time+12'), ('Pacific/Fiji', '(IST+12:00) Fiji'), ('Asia/Anadyr', '(IST+12:00) Magadan'), ('Asia/Kamchatka', '(IST+12:00) Petropavlovsk-Kamchatsky - Old'), ('Etc/GMT-13', "(IST+13:00) Nuku'alofa"), ('Pacific/Apia', '(IST+13:00) Samoa')], default='IST', max_length=50)),
                ('time_format', models.CharField(choices=[('HH:MM AM/PM', 'HH:MM AM/PM (e.g., 08:15 PM)'), ('HH:MM', 'HH:MM (24-hour format, e.g., 20:15)')], default='HH:MM AM/PM', max_length=20)),
                ('decimal_places', models.PositiveIntegerField(default=2)),
                ('login_attempts', models.PositiveIntegerField(default=5)),
                ('two_factor_authentication', models.BooleanField(default=False)),
                ('currency', models.CharField(choices=[('EUR', 'EUR - Andorra'), ('AED', 'AED - United Arab Emirates'), ('AFN', 'AFN - Afghanistan'), ('XCD', 'XCD - Antigua and Barbuda'), ('XCD', 'XCD - Anguilla'), ('ALL', 'ALL - Albania'), ('AMD', 'AMD - Armenia'), ('AOA', 'AOA - Angola'), ('ARS', 'ARS - Argentina'), ('USD', 'USD - American Samoa'), ('EUR', 'EUR - Austria'), ('AUD', 'AUD - Australia'), ('AWG', 'AWG - Aruba'), ('EUR', 'EUR - Aland'), ('AZN', 'AZN - Azerbaijan'), ('BAM', 'BAM - Bosnia and Herzegovina'), ('BBD', 'BBD - Barbados'), ('BDT', 'BDT - Bangladesh'), ('EUR', 'EUR - Belgium'), ('XOF', 'XOF - Burkina Faso'), ('BGN', 'BGN - Bulgaria'), ('BHD', 'BHD - Bahrain'), ('BIF', 'BIF - Burundi'), ('XOF', 'XOF - Benin'), ('EUR', 'EUR - Saint Barthelemy'), ('BMD', 'BMD - Bermuda'), ('BND', 'BND - Brunei'), ('BOB', 'BOB - Bolivia'), ('BOV', 'BOV - Bolivia'), ('USD', 'USD - Bonaire'), ('BRL', 'BRL - Brazil'), ('BSD', 'BSD - Bahamas'), ('BTN', 'BTN - Bhutan'), ('INR', 'INR - Bhutan'), ('NOK', 'NOK - Bouvet Island'), ('BWP', 'BWP - Botswana'), ('BYN', 'BYN - Belarus'), ('BZD', 'BZD - Belize'), ('CAD', 'CAD - Canada'), ('AUD', 'AUD - Cocos (Keeling) Islands'), ('CDF', 'CDF - Democratic Republic of the Congo'), ('XAF', 'XAF - Central African Republic'), ('XAF', 'XAF - Republic of the Congo'), ('CHE', 'CHE - Switzerland'), ('CHF', 'CHF - Switzerland'), ('CHW', 'CHW - Switzerland'), ('XOF', 'XOF - Ivory Coast'), ('NZD', 'NZD - Cook Islands'), ('CLF', 'CLF - Chile'), ('CLP', 'CLP - Chile'), ('XAF', 'XAF - Cameroon'), ('CNY', 'CNY - China'), ('COP', 'COP - Colombia'), ('CRC', 'CRC - Costa Rica'), ('CUC', 'CUC - Cuba'), ('CUP', 'CUP - Cuba'), ('CVE', 'CVE - Cape Verde'), ('ANG', 'ANG - Curacao'), ('AUD', 'AUD - Christmas Island'), ('EUR', 'EUR - Cyprus'), ('CZK', 'CZK - Czech Republic'), ('EUR', 'EUR - Germany'), ('DJF', 'DJF - Djibouti'), ('DKK', 'DKK - Denmark'), ('XCD', 'XCD - Dominica'), ('DOP', 'DOP - Dominican Republic'), ('DZD', 'DZD - Algeria'), ('USD', 'USD - Ecuador'), ('EUR', 'EUR - Estonia'), ('EGP', 'EGP - Egypt'), ('MAD', 'MAD - Western Sahara'), ('DZD', 'DZD - Western Sahara'), ('MRU', 'MRU - Western Sahara'), ('ERN', 'ERN - Eritrea'), ('EUR', 'EUR - Spain'), ('ETB', 'ETB - Ethiopia'), ('EUR', 'EUR - Finland'), ('FJD', 'FJD - Fiji'), ('FKP', 'FKP - Falkland Islands'), ('USD', 'USD - Micronesia'), ('DKK', 'DKK - Faroe Islands'), ('EUR', 'EUR - France'), ('XAF', 'XAF - Gabon'), ('GBP', 'GBP - United Kingdom'), ('XCD', 'XCD - Grenada'), ('GEL', 'GEL - Georgia'), ('EUR', 'EUR - French Guiana'), ('GBP', 'GBP - Guernsey'), ('GHS', 'GHS - Ghana'), ('GIP', 'GIP - Gibraltar'), ('DKK', 'DKK - Greenland'), ('GMD', 'GMD - Gambia'), ('GNF', 'GNF - Guinea'), ('EUR', 'EUR - Guadeloupe'), ('XAF', 'XAF - Equatorial Guinea'), ('EUR', 'EUR - Greece'), ('GBP', 'GBP - South Georgia and the South Sandwich Islands'), ('GTQ', 'GTQ - Guatemala'), ('USD', 'USD - Guam'), ('XOF', 'XOF - Guinea-Bissau'), ('GYD', 'GYD - Guyana'), ('HKD', 'HKD - Hong Kong'), ('AUD', 'AUD - Heard Island and McDonald Islands'), ('HNL', 'HNL - Honduras'), ('EUR', 'EUR - Croatia'), ('HTG', 'HTG - Haiti'), ('USD', 'USD - Haiti'), ('HUF', 'HUF - Hungary'), ('IDR', 'IDR - Indonesia'), ('EUR', 'EUR - Ireland'), ('ILS', 'ILS - Israel'), ('GBP', 'GBP - Isle of Man'), ('INR', 'INR - India'), ('USD', 'USD - British Indian Ocean Territory'), ('IQD', 'IQD - Iraq'), ('IRR', 'IRR - Iran'), ('ISK', 'ISK - Iceland'), ('EUR', 'EUR - Italy'), ('GBP', 'GBP - Jersey'), ('JMD', 'JMD - Jamaica'), ('JOD', 'JOD - Jordan'), ('JPY', 'JPY - Japan'), ('KES', 'KES - Kenya'), ('KGS', 'KGS - Kyrgyzstan'), ('KHR', 'KHR - Cambodia'), ('AUD', 'AUD - Kiribati'), ('KMF', 'KMF - Comoros'), ('XCD', 'XCD - Saint Kitts and Nevis'), ('KPW', 'KPW - North Korea'), ('KRW', 'KRW - South Korea'), ('KWD', 'KWD - Kuwait'), ('KYD', 'KYD - Cayman Islands'), ('KZT', 'KZT - Kazakhstan'), ('LAK', 'LAK - Laos'), ('LBP', 'LBP - Lebanon'), ('XCD', 'XCD - Saint Lucia'), ('CHF', 'CHF - Liechtenstein'), ('LKR', 'LKR - Sri Lanka'), ('LRD', 'LRD - Liberia'), ('LSL', 'LSL - Lesotho'), ('ZAR', 'ZAR - Lesotho'), ('EUR', 'EUR - Lithuania'), ('EUR', 'EUR - Luxembourg'), ('EUR', 'EUR - Latvia'), ('LYD', 'LYD - Libya'), ('MAD', 'MAD - Morocco'), ('EUR', 'EUR - Monaco'), ('MDL', 'MDL - Moldova'), ('EUR', 'EUR - Montenegro'), ('EUR', 'EUR - Saint Martin'), ('MGA', 'MGA - Madagascar'), ('USD', 'USD - Marshall Islands'), ('MKD', 'MKD - North Macedonia'), ('XOF', 'XOF - Mali'), ('MMK', 'MMK - Myanmar (Burma)'), ('MNT', 'MNT - Mongolia'), ('MOP', 'MOP - Macao'), ('USD', 'USD - Northern Mariana Islands'), ('EUR', 'EUR - Martinique'), ('MRU', 'MRU - Mauritania'), ('XCD', 'XCD - Montserrat'), ('EUR', 'EUR - Malta'), ('MUR', 'MUR - Mauritius'), ('MVR', 'MVR - Maldives'), ('MWK', 'MWK - Malawi'), ('MXN', 'MXN - Mexico'), ('MYR', 'MYR - Malaysia'), ('MZN', 'MZN - Mozambique'), ('NAD', 'NAD - Namibia'), ('ZAR', 'ZAR - Namibia'), ('XPF', 'XPF - New Caledonia'), ('XOF', 'XOF - Niger'), ('AUD', 'AUD - Norfolk Island'), ('NGN', 'NGN - Nigeria'), ('NIO', 'NIO - Nicaragua'), ('EUR', 'EUR - Netherlands'), ('NOK', 'NOK - Norway'), ('NPR', 'NPR - Nepal'), ('AUD', 'AUD - Nauru'), ('NZD', 'NZD - Niue'), ('NZD', 'NZD - New Zealand'), ('OMR', 'OMR - Oman'), ('PAB', 'PAB - Panama'), ('USD', 'USD - Panama'), ('PEN', 'PEN - Peru'), ('XPF', 'XPF - French Polynesia'), ('PGK', 'PGK - Papua New Guinea'), ('PHP', 'PHP - Philippines'), ('PKR', 'PKR - Pakistan'), ('PLN', 'PLN - Poland'), ('EUR', 'EUR - Saint Pierre and Miquelon'), ('NZD', 'NZD - Pitcairn Islands'), ('USD', 'USD - Puerto Rico'), ('ILS', 'ILS - Palestine'), ('EUR', 'EUR - Portugal'), ('USD', 'USD - Palau'), ('PYG', 'PYG - Paraguay'), ('QAR', 'QAR - Qatar'), ('EUR', 'EUR - Reunion'), ('RON', 'RON - Romania'), ('RSD', 'RSD - Serbia'), ('RUB', 'RUB - Russia'), ('RWF', 'RWF - Rwanda'), ('SAR', 'SAR - Saudi Arabia'), ('SBD', 'SBD - Solomon Islands'), ('SCR', 'SCR - Seychelles'), ('SDG', 'SDG - Sudan'), ('SEK', 'SEK - Sweden'), ('SGD', 'SGD - Singapore'), ('SHP', 'SHP - Saint Helena'), ('EUR', 'EUR - Slovenia'), ('NOK', 'NOK - Svalbard and Jan Mayen'), ('EUR', 'EUR - Slovakia'), ('SLL', 'SLL - Sierra Leone'), ('EUR', 'EUR - San Marino'), ('XOF', 'XOF - Senegal'), ('SOS', 'SOS - Somalia'), ('SRD', 'SRD - Suriname'), ('SSP', 'SSP - South Sudan'), ('STN', 'STN - Sao Tome and Principe'), ('SVC', 'SVC - El Salvador'), ('USD', 'USD - El Salvador'), ('ANG', 'ANG - Sint Maarten'), ('SYP', 'SYP - Syria'), ('SZL', 'SZL - Eswatini'), ('USD', 'USD - Turks and Caicos Islands'), ('XAF', 'XAF - Chad'), ('EUR', 'EUR - French Southern Territories'), ('XOF', 'XOF - Togo'), ('THB', 'THB - Thailand'), ('TJS', 'TJS - Tajikistan'), ('NZD', 'NZD - Tokelau'), ('USD', 'USD - East Timor'), ('TMT', 'TMT - Turkmenistan'), ('TND', 'TND - Tunisia'), ('TOP', 'TOP - Tonga'), ('TRY', 'TRY - Turkey'), ('TTD', 'TTD - Trinidad and Tobago'), ('AUD', 'AUD - Tuvalu'), ('TWD', 'TWD - Taiwan'), ('TZS', 'TZS - Tanzania'), ('UAH', 'UAH - Ukraine'), ('UGX', 'UGX - Uganda'), ('USD', 'USD - U.S. Minor Outlying Islands'), ('USD', 'USD - United States'), ('UYI', 'UYI - Uruguay'), ('UYU', 'UYU - Uruguay'), ('UZS', 'UZS - Uzbekistan'), ('EUR', 'EUR - Vatican City'), ('XCD', 'XCD - Saint Vincent and the Grenadines'), ('VES', 'VES - Venezuela'), ('USD', 'USD - British Virgin Islands'), ('USD', 'USD - U.S. Virgin Islands'), ('VND', 'VND - Vietnam'), ('VUV', 'VUV - Vanuatu'), ('XPF', 'XPF - Wallis and Futuna'), ('WST', 'WST - Samoa'), ('EUR', 'EUR - Kosovo'), ('YER', 'YER - Yemen'), ('EUR', 'EUR - Mayotte'), ('ZAR', 'ZAR - South Africa'), ('ZMW', 'ZMW - Zambia'), ('USD', 'USD - Zimbabwe'), ('ZAR', 'ZAR - Zimbabwe'), ('BWP', 'BWP - Zimbabwe'), ('GBP', 'GBP - Zimbabwe'), ('AUD', 'AUD - Zimbabwe'), ('CNY', 'CNY - Zimbabwe'), ('INR', 'INR - Zimbabwe'), ('JPY', 'JPY - Zimbabwe')], default='USD', max_length=10)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='systemconfiguration_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='systemconfiguration_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'System Configuration',
                'verbose_name_plural': 'System Configurations',
            },
        ),
        migrations.CreateModel(
            name='PasswordPolicies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('min_length', models.IntegerField(blank=True, default=4, null=True)),
                ('min_uppercase', models.IntegerField(blank=True, default=1, null=True)),
                ('min_lowercase', models.IntegerField(blank=True, default=1, null=True)),
                ('min_numerals', models.IntegerField(blank=True, default=1, null=True)),
                ('min_special_chars', models.IntegerField(blank=True, default=1, null=True)),
                ('password_hint', models.TextField(blank=True, null=True, verbose_name='Password Hint')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passwordpolicies_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passwordpolicies_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]