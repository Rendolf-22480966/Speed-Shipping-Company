"""Structured content for each Speed-Shipping service detail page."""

SERVICES = {
    'cash-in-transit': {
        'title': 'Cash in Transit (CIT)',
        'tagline': 'Armored collection, GPS-monitored transportation and verified delivery of cash and valuables — nationwide.',
        'hero_image': 'services/cash-in-transit/hero.png',
        'hero_position': 'center 45%',
        'premium': True,
        'what_it_means': (
            'Cash in Transit (CIT) is the secure collection, transportation and delivery of cash, coin '
            'and other negotiable valuables between banks, retail outlets, ATMs, casinos, government '
            'facilities and cash processing centres. Every movement is executed in specially equipped '
            'armored vehicles by vetted security personnel, with real-time GPS tracking and documented '
            'chain-of-custody from the moment of collection through to verified handover at destination.'
        ),
        'overview_points': [
            'Dual-crew armored vehicles with tamper-resistant cash compartments',
            'Live GPS tracking and 24/7 control-room monitoring on every route',
            'Signed chain-of-custody records at each collection and delivery point',
            'Route risk assessments conducted before every scheduled and ad-hoc movement',
        ],
        'security_protocols': [
            {
                'title': 'Armored Fleet & Vehicle Security',
                'text': (
                    'Our CIT fleet comprises ballistic-rated armored vehicles fitted with dual-lock '
                    'compartments, anti-jamming communications and tamper-alert systems. Vehicles are '
                    'maintained to strict security standards and never carry mixed client consignments '
                    'without explicit authorisation.'
                ),
            },
            {
                'title': 'GPS Tracking & Control-Room Monitoring',
                'text': (
                    'Every vehicle is equipped with real-time GPS tracking linked to our 24/7 operations '
                    'control centre. Supervisors monitor route adherence, dwell times and exception alerts '
                    '— enabling immediate response to any deviation from the approved plan.'
                ),
            },
            {
                'title': 'Vetted Personnel & Escort Protocols',
                'text': (
                    'All CIT crews undergo enhanced background screening, specialist training and regular '
                    're-certification. Where jurisdiction and client risk profile require it, armed '
                    'security escorts are deployed with continuous radio contact to the control room.'
                ),
            },
            {
                'title': 'Chain-of-Custody & Delivery Verification',
                'text': (
                    'Each consignment is sealed, logged and signed for at every handover point. Delivery '
                    'verification includes recipient identification, dual-signature confirmation and '
                    'electronic upload of custody records to your secure client portal.'
                ),
            },
        ],
        'editorial_blocks': [
            {
                'title': 'Professional Security Escorts',
                'body': (
                    'High-value cash movements demand more than transport — they require trained '
                    'protection. Our security escorts are deployed on routes classified medium-to-high '
                    'risk, maintaining unbroken chain-of-custody and secure communications with our '
                    'operations centre throughout the journey.'
                ),
                'highlights': [
                    'Enhanced background screening and ongoing vetting for all personnel',
                    'Armed escort deployment where jurisdiction and risk profile require it',
                    'Continuous radio and GPS-linked contact with the 24/7 control room',
                    'Documented handover procedures at every collection and delivery point',
                ],
                'image': 'services/cash-in-transit/escort.png',
                'reverse': False,
            },
            {
                'title': 'Specially Equipped Armored Fleet',
                'body': (
                    'Our armored vehicles are purpose-built for cash logistics — not adapted from '
                    'standard commercial stock. Tamper-resistant compartments, specialist loading systems '
                    'and live GPS telemetry ensure secure handling at banks, retail locations, ATMs and '
                    'central cash processing facilities.'
                ),
                'highlights': [
                    'Ballistic-rated bodies with dual-lock, segregated cash compartments',
                    'Real-time GPS tracking with geofencing and route-deviation alerts',
                    'Tamper-evident seals applied and logged at every loading point',
                    'Preventative maintenance schedules aligned to security audit requirements',
                ],
                'image': 'services/cash-in-transit/equipment.png',
                'reverse': True,
            },
        ],
        'gallery': [],
        'clients_heading': 'Typical Clients',
        'clients': [
            'Banks and building societies',
            'Retail chains and shopping malls',
            'Hotels, casinos and entertainment venues',
            'Government agencies and public-sector bodies',
            'Independent ATM operators',
            'Cash processing and recycling centres',
        ],
        'features_heading': 'What It Includes',
        'features': [
            'Scheduled and ad-hoc armored cash collection',
            'Secure transportation in GPS-monitored armored vehicles',
            'Armed security escorts (where applicable by jurisdiction)',
            'Real-time GPS tracking and 24/7 control-room oversight',
            'Tamper-evident sealing and chain-of-custody documentation',
            'Dual-signature delivery verification at destination',
            'Route risk assessment before every movement',
            'Insured carriage with full audit-trail reporting',
        ],
    },
    'cash-management': {
        'title': 'Cash Management',
        'tagline': 'Secure counting, authentication, storage and deposit preparation — from collection to bank-ready funds.',
        'hero_image': 'services/cash-management/hero.png',
        'premium': True,
        'what_it_means': (
            'Cash Management is the complete handling of a client\'s physical cash after collection. '
            'Instead of simply transporting money, the company counts, verifies, sorts, authenticates, '
            'stores, and prepares funds for deposit or redistribution — all within access-controlled '
            'processing environments monitored by CCTV and governed by strict dual-control procedures.'
        ),
        'overview_points': [
            'UV, magnetic and infrared counterfeit detection on every note processed',
            'Segregated processing rooms with controlled access and CCTV coverage',
            'Dual-control procedures — no single operator handles funds alone',
            'Secure reporting and deposit preparation aligned to your banking specifications',
        ],
        'security_protocols': [
            {
                'title': 'Controlled Processing Environment',
                'text': (
                    'All cash processing takes place in secure, access-controlled facilities. Entry is '
                    'restricted to authorised personnel via biometric and PIN verification. Processing '
                    'areas are monitored 24/7 by CCTV with recordings retained in accordance with '
                    'regulatory and client audit requirements.'
                ),
            },
            {
                'title': 'Counterfeit Detection & Authentication',
                'text': (
                    'Every note passes through multi-layer authentication — ultraviolet, magnetic and '
                    'infrared detection — before being counted and sorted. Suspect items are quarantined, '
                    'logged and reported through a documented escalation procedure.'
                ),
            },
            {
                'title': 'Secure Storage & Segregation',
                'text': (
                    'Processed funds are held in locked, alarmed storage until deposit dispatch. Client '
                    'funds are segregated at all times — never commingled — with inventory counts '
                    'reconciled at the start and end of every processing cycle.'
                ),
            },
            {
                'title': 'Reconciliation & Secure Reporting',
                'text': (
                    'Automated counting systems generate tamper-proof transaction reports showing '
                    'denomination breakdowns, totals and variance analysis. Reports are delivered '
                    'securely via encrypted client portals or signed physical documentation.'
                ),
            },
        ],
        'editorial_blocks': [
            {
                'title': 'Precision Cash Processing',
                'body': (
                    'Our cash processing centres operate to banking-grade standards. High-speed counting '
                    'and sorting equipment is calibrated daily, and every batch is reconciled against '
                    'declared collection totals before deposit preparation begins — eliminating '
                    'shrinkage and reducing your administrative burden.'
                ),
                'highlights': [
                    'Multi-denomination counting with automated batch reporting',
                    'UV/MG/IR counterfeit detection on every note processed',
                    'Currency sorting by denomination, condition and fitness for reissue',
                    'Variance reporting with full audit trail for treasury teams',
                ],
                'image': 'services/cash-management/detail-2.png',
                'reverse': False,
            },
            {
                'title': 'Retail & Institutional Integration',
                'body': (
                    'From national supermarket chains to private banks, we integrate with your existing '
                    'treasury workflows. Secure collection schedules, provisional credit options and '
                    'consistent service-level agreements ensure cash flows smoothly from point-of-sale '
                    'to deposit — without exposing your staff or premises to unnecessary risk.'
                ),
                'highlights': [
                    'Scheduled collections tailored to peak trading periods',
                    'Provisional credit to improve cash-flow visibility',
                    'Secure reporting delivered via encrypted client portals',
                    'Multi-site reconciliation across your entire estate',
                ],
                'image': 'services/cash-management/detail-1.png',
                'reverse': True,
            },
        ],
        'gallery': [],
        'clients_heading': 'Typical Clients',
        'clients': [
            'Banks and credit unions',
            'Supermarkets and hypermarkets',
            'Large retailers and department stores',
            'Restaurants and hospitality groups',
            'Fuel stations and convenience chains',
            'Entertainment and leisure venues',
        ],
        'features_heading': 'Services Include',
        'features': [
            'High-speed cash counting and denomination sorting',
            'UV, magnetic and infrared counterfeit detection',
            'Deposit preparation to your exact banking specifications',
            'Cash reconciliation with variance and audit reporting',
            'Secure interim storage in alarmed, access-controlled vaults',
            'Dual-control processing — two authorised operators at all times',
            'Encrypted secure reporting via client portal or signed documentation',
            'Provisional credit and treasury integration options',
        ],
    },
    'secure-cash-mailing': {
        'title': 'Secure Cash Mailing',
        'tagline': 'Tamper-evident packaging, full GPS-tracked custody and insured delivery of cash and negotiable instruments.',
        'hero_image': 'services/secure-cash-mailing/hero.png',
        'premium': True,
        'what_it_means': (
            'Secure Cash Mailing is the protected shipment of cash, bank drafts, certified cheques, '
            'negotiable instruments and confidential financial documents. Unlike standard postal services, '
            'every consignment travels in tamper-evident packaging under documented chain-of-custody, '
            'with GPS-tracked vehicles, delivery confirmation and optional full-value insurance coverage.'
        ),
        'overview_points': [
            'Tamper-evident, numbered seals applied and logged at origin',
            'GPS-tracked secure vehicles — never routed through public postal networks',
            'Dual-signature delivery confirmation with recipient identity verification',
            'Optional full-value insurance underwritten by accredited carriers',
        ],
        'security_protocols': [
            {
                'title': 'Tamper-Evident Packaging',
                'text': (
                    'Consignments are sealed in numbered, tamper-evident bags or containers at the point '
                    'of collection. Seal numbers are recorded in the chain-of-custody log and verified '
                    'intact at every checkpoint and at final delivery. Any seal compromise triggers '
                    'immediate escalation to our security operations centre.'
                ),
            },
            {
                'title': 'Chain-of-Custody Documentation',
                'text': (
                    'Every handover — from sender to courier, courier to transit hub, and hub to recipient '
                    '— is logged with timestamp, operator identity and signature. Full custody records '
                    'are available for audit, dispute resolution and regulatory compliance.'
                ),
            },
            {
                'title': 'GPS-Tracked Secure Transport',
                'text': (
                    'Consignments travel exclusively in GPS-monitored secure vehicles operated by vetted '
                    'couriers. Routes are pre-approved following risk assessment, and real-time tracking '
                    'is available to authorised client contacts via our secure portal.'
                ),
            },
            {
                'title': 'Delivery Confirmation & Insurance',
                'text': (
                    'Delivery is confirmed by recipient identity verification and dual-signature receipt. '
                    'Optional full-value insurance covers loss, theft or damage in transit — underwritten '
                    'by accredited carriers with certificates issued per consignment.'
                ),
            },
        ],
        'editorial_blocks': [
            {
                'title': 'Tamper-Evident Custody Chain',
                'body': (
                    'From the moment your consignment is sealed at origin, every movement is documented. '
                    'Our couriers carry encrypted handheld devices that log each custody transfer in '
                    'real time — giving you and your auditors a complete, timestamped record from '
                    'collection through to verified delivery.'
                ),
                'highlights': [
                    'Numbered tamper-evident seals logged at collection',
                    'Real-time custody updates via encrypted courier devices',
                    'Checkpoint verification at every transit stage',
                    'Immediate escalation if seal integrity is compromised',
                ],
                'image': 'services/secure-cash-mailing/detail-1.png',
                'reverse': False,
            },
            {
                'title': 'International & Confidential Handling',
                'body': (
                    'Financial institutions, government offices and corporate treasuries rely on our '
                    'mailing service for discreet movement of physical funds and instruments across '
                    'domestic and international routes — without exposure to standard postal or courier '
                    'networks that lack appropriate security controls.'
                ),
                'highlights': [
                    'Door-to-door collection and delivery by vetted couriers',
                    'International routing via approved secure logistics partners',
                    'Confidential handling — consignment contents never disclosed to third parties',
                    'Full-value insurance options for high-value instruments',
                ],
                'image': 'services/secure-cash-mailing/detail-2.png',
                'reverse': True,
            },
        ],
        'gallery': [],
        'clients_heading': 'Typical Clients',
        'clients': [
            'Banks and financial institutions',
            'Government departments and agencies',
            'Corporate treasury and finance teams',
            'International businesses and trade finance houses',
            'Legal firms handling settlement funds',
            'Insurance and claims settlement bodies',
        ],
        'features_heading': 'Features Include',
        'features': [
            'Tamper-evident numbered seals and secure packaging',
            'Full GPS-tracked chain-of-custody on every consignment',
            'Dual-signature delivery confirmation with ID verification',
            'Confidential handling by vetted, uniformed couriers',
            'Real-time tracking via secure client portal',
            'Optional full-value transit insurance per consignment',
            'Domestic and international secure routing',
            'Complete audit-trail documentation for compliance',
        ],
    },
    'atm-services': {
        'title': 'ATM Services',
        'tagline': 'Secure cassette loading, GPS-monitored replenishment and 24/7 monitoring for your ATM network.',
        'hero_image': 'services/atm-services/hero.png',
        'premium': True,
        'what_it_means': (
            'ATM Services cover everything required to keep automated teller machines operational — '
            'including secure cash replenishment, cassette balancing, maintenance coordination, '
            'first-line technical support and remote monitoring. Cash cassettes are loaded in '
            'controlled environments, transported in GPS-tracked armored vehicles and installed under '
            'dual-control procedures to maintain security and uptime across your entire network.'
        ),
        'overview_points': [
            'Cassettes loaded in secure, access-controlled cash processing facilities',
            'GPS-monitored armored delivery to every terminal on your network',
            'Dual-control loading — two authorised operators present at all times',
            'Remote monitoring with automated alerts for faults, low cash and tamper events',
        ],
        'security_protocols': [
            {
                'title': 'Secure Cassette Preparation',
                'text': (
                    'ATM cassettes are loaded in dedicated, access-controlled areas separate from general '
                    'cash processing. Denomination mixes are verified by dual operators, sealed with '
                    'tamper-evident tags and logged against terminal ID and scheduled service date before '
                    'dispatch.'
                ),
            },
            {
                'title': 'GPS-Monitored Replenishment Routes',
                'text': (
                    'Loaded cassettes travel in GPS-tracked armored vehicles on pre-approved routes. '
                    'Our control room monitors every replenishment run in real time, with geofencing '
                    'alerts if a vehicle deviates from its assigned route or exceeds permitted dwell time.'
                ),
            },
            {
                'title': 'Dual-Control Terminal Access',
                'text': (
                    'Cassette swap operations at the ATM require two authorised technicians — one to '
                    'handle the secure compartment, one to verify and sign off. Empty cassettes are '
                    'sealed immediately and returned for counting and reconciliation under CCTV.'
                ),
            },
            {
                'title': 'Remote Monitoring & Emergency Response',
                'text': (
                    'Our monitoring centre tracks terminal status, cash levels and hardware alerts across '
                    'your network 24/7. First-line maintenance teams and emergency response crews are '
                    'dispatched within agreed SLA windows to resolve faults before they affect customers.'
                ),
            },
        ],
        'editorial_blocks': [
            {
                'title': 'Scheduled Cash Replenishment',
                'body': (
                    'We analyse transaction data and seasonal patterns to forecast cash demand across '
                    'your ATM estate — minimising both outages and excess float. Replenishment schedules '
                    'are optimised for airports, shopping centres, hospitals, university campuses and '
                    'branch networks, with emergency top-up capability for unplanned surges.'
                ),
                'highlights': [
                    'Data-driven cash forecasting by terminal and location',
                    'Flexible scheduling — daily, weekly or event-driven replenishment',
                    'Emergency top-up response within agreed SLA windows',
                    'Reduced float costs through optimised denomination mixes',
                ],
                'image': 'services/atm-services/detail-1.png',
                'reverse': False,
            },
            {
                'title': 'Specialist Loading & Field Operations',
                'body': (
                    'Our field teams carry specialist loading equipment and operate under strict '
                    'security protocols at every terminal. GPS-monitored routes, tamper-evident cassette '
                    'seals and dual-control swap procedures ensure cassettes reach each machine securely '
                    'and are reconciled accurately after collection.'
                ),
                'highlights': [
                    'Armored GPS-tracked vehicles for all cassette movements',
                    'Tamper-evident seals verified at loading and terminal swap',
                    'First-line maintenance to resolve faults on-site',
                    'Full cassette reconciliation with variance reporting',
                ],
                'image': 'services/atm-services/detail-2.png',
                'reverse': True,
            },
        ],
        'gallery': [],
        'clients_heading': 'Typical Clients',
        'clients': [
            'Banks and independent ATM deployers',
            'Airports and transport hubs',
            'Shopping centres and retail parks',
            'Universities and campus operators',
            'Hospitals and healthcare trusts',
            'Leisure and entertainment venues',
        ],
        'features_heading': 'Services Include',
        'features': [
            'Secure ATM cassette loading in controlled facilities',
            'GPS-monitored armored replenishment routes',
            'Cash forecasting and optimised denomination planning',
            'Scheduled and emergency replenishment programmes',
            'Dual-control cassette swap at every terminal',
            'First-line maintenance and hardware fault resolution',
            '24/7 remote terminal monitoring and alert management',
            'Emergency response teams with agreed SLA commitments',
        ],
    },
    'vaulting-custody': {
        'title': 'Vaulting & Custody',
        'tagline': 'Biometric-controlled vault storage, 24/7 CCTV surveillance and fully auditable custody records.',
        'hero_image': 'services/vaulting-custody/hero.png',
        'premium': True,
        'what_it_means': (
            'Vaulting and Custody provide highly secure, allocated storage for valuable assets in '
            'monitored vault facilities with controlled access and detailed custody records. Clients '
            'receive segregated vault space protected by multi-layer security — biometric access '
            'controls, 24/7 CCTV surveillance, alarmed compartments and climate-controlled environments '
            'where required — with every deposit, inspection and withdrawal logged for audit.'
        ),
        'overview_points': [
            'Allocated, segregated vault space — your assets never commingled with others',
            'Biometric and dual-authorisation access controls on every vault entry',
            '24/7 CCTV surveillance with retained recordings for audit purposes',
            'Climate-controlled storage available for art, documents and sensitive materials',
        ],
        'security_protocols': [
            {
                'title': 'Multi-Layer Vault Infrastructure',
                'text': (
                    'Our vault facilities feature reinforced construction, time-delay locks and '
                    'intruder-detection systems integrated with a 24/7 alarm receiving centre. Vault '
                    'chambers are subdivided into individually lockable compartments, each allocated '
                    'exclusively to a single client.'
                ),
            },
            {
                'title': 'Biometric Access & Dual Control',
                'text': (
                    'Entry to vault areas requires biometric verification (fingerprint or retinal scan) '
                    'combined with PIN or smart-card authentication. All access attempts — authorised '
                    'and denied — are logged with timestamp and operator identity. Client withdrawals '
                    'require dual authorisation and pre-booked appointment slots.'
                ),
            },
            {
                'title': '24/7 Surveillance & Alarm Monitoring',
                'text': (
                    'Every vault facility is monitored continuously by CCTV with pan-tilt-zoom coverage '
                    'of all access points, corridors and storage areas. Recordings are retained in '
                    'accordance with regulatory requirements and made available for client audit on '
                    'request. Alarm signals are routed to our security operations centre and, where '
                    'contracted, to local law enforcement.'
                ),
            },
            {
                'title': 'Auditable Custody Records',
                'text': (
                    'Every asset deposit, inspection and withdrawal generates a signed custody record '
                    'with item description, weight or count, condition notes and authorising signatures. '
                    'Records are maintained in secure digital archives with optional client portal access '
                    'for real-time custody visibility.'
                ),
            },
        ],
        'editorial_blocks': [
            {
                'title': 'High-Security Vault Infrastructure',
                'body': (
                    'Our vault facilities are engineered to protect bullion, cash reserves, jewellery, '
                    'diamonds, fine art and confidential documents. Reinforced vault chambers, time-delay '
                    'locking mechanisms and segregated client compartments ensure that your assets remain '
                    'physically isolated and protected at all times — with no commingling between clients.'
                ),
                'highlights': [
                    'Reinforced vault construction with time-delay lock systems',
                    'Individually allocated, lockable client compartments',
                    'Biometric and smart-card access on every vault entry',
                    'Intruder detection linked to 24/7 alarm receiving centre',
                ],
                'image': 'services/vaulting-custody/detail-1.png',
                'reverse': False,
            },
            {
                'title': 'Climate-Controlled & Specialist Storage',
                'body': (
                    'Certain assets demand more than security — they require environmental protection. '
                    'Climate-controlled vault zones maintain regulated temperature and humidity for fine '
                    'art, rare documents, luxury watches and other sensitive items. Custody records '
                    'document environmental conditions at deposit and at every scheduled inspection.'
                ),
                'highlights': [
                    'Temperature and humidity-controlled storage zones',
                    'Specialist racking for art, bullion and document archives',
                    'Scheduled inspection reports with condition photography',
                    'Insurance appraisal support and certificate storage',
                ],
                'image': 'services/vaulting-custody/detail-2.png',
                'reverse': True,
            },
        ],
        'gallery': [],
        'clients_heading': 'Typical Assets',
        'clients': [
            'Gold and silver bullion',
            'Cash reserves and currency holdings',
            'Diamonds, gemstones and jewellery',
            'Fine art and cultural artefacts',
            'Confidential documents and legal deeds',
            'Luxury watches and collectibles',
        ],
        'features_heading': 'Features Include',
        'features': [
            'Allocated, segregated high-security vault compartments',
            'Biometric and dual-authorisation access controls',
            '24/7 CCTV surveillance with audit-ready recordings',
            'Climate-controlled environments for sensitive assets',
            'Time-delay locks and intruder-detection alarm systems',
            'Auditable custody records for every deposit and withdrawal',
            'Optional full-value insurance arranged through accredited underwriters',
            'Secure client portal for real-time custody visibility',
        ],
    },
    'precious-goods-transport': {
        'title': 'Precious Goods Transport',
        'tagline': 'GPS-tracked, armoured transport of diamonds, bullion, watches and fine art with full chain-of-custody.',
        'hero_image': 'services/precious-goods-transport/hero.png',
        'premium': True,
        'what_it_means': (
            'Precious Goods Transport specialises in the secure movement of high-value items that '
            'demand exceptional protection and discreet handling — including gold, diamonds, luxury '
            'watches, jewellery, fine art and rare collectibles. Every consignment receives a '
            'pre-movement risk assessment, specialist tamper-evident packaging, GPS-tracked routing '
            'and documented chain-of-custody, with optional armed escort depending on jurisdiction '
            'and client requirements.'
        ),
        'overview_points': [
            'Pre-movement route and threat assessment for every consignment',
            'Specialist tamper-evident packaging designed for high-value goods',
            'Real-time GPS tracking with control-room monitoring throughout transit',
            'Full chain-of-custody documentation from collection to verified delivery',
        ],
        'security_protocols': [
            {
                'title': 'Risk Assessment & Secure Routing',
                'text': (
                    'Before any movement, our security analysts conduct a route and threat assessment '
                    'considering value, geography, timing and client profile. Routes are approved by '
                    'operations control and may include varied timing, multi-vehicle protocols or '
                    'armed escort where the assessment requires it.'
                ),
            },
            {
                'title': 'Specialist Packaging & Sealing',
                'text': (
                    'High-value items are packed in purpose-designed, tamper-evident containers appropriate '
                    'to the asset type — shock-resistant cases for watches and jewellery, climate-aware '
                    'crating for art, and sealed bullion containers for precious metals. Every package '
                    'is numbered, photographed and logged before dispatch.'
                ),
            },
            {
                'title': 'GPS Tracking & Live Monitoring',
                'text': (
                    'All precious goods vehicles carry real-time GPS tracking linked to our 24/7 control '
                    'room. Supervisors monitor progress against approved routes and receive automated '
                    'alerts for deviations, unscheduled stops or geofence breaches — enabling immediate '
                    'intervention if required.'
                ),
            },
            {
                'title': 'Chain-of-Custody & Armed Escort',
                'text': (
                    'Every handover is documented with operator identity, timestamp and signature. '
                    'Where jurisdiction and client requirements permit, armed security escorts accompany '
                    'consignments classified as highest risk — maintaining continuous contact with the '
                    'control room and following pre-approved contingency protocols.'
                ),
            },
        ],
        'editorial_blocks': [
            {
                'title': 'Certified Gemstone & Jewellery Logistics',
                'body': (
                    'Diamond merchants, jewellers and luxury retailers depend on our secure carriage for '
                    'domestic and international consignments. We provide customs facilitation, insured '
                    'transport and specialist packaging — with full chain-of-custody documentation '
                    'suitable for Kimberley Process compliance and insurer audit requirements.'
                ),
                'highlights': [
                    'Specialist tamper-evident packaging for gems and jewellery',
                    'Customs clearance and international secure routing',
                    'Insured carriage with certificates per consignment',
                    'Chain-of-custody records for regulatory and insurer audit',
                ],
                'image': 'services/precious-goods-transport/detail-1.png',
                'reverse': False,
            },
            {
                'title': 'Air, Road & International Freight',
                'body': (
                    'High-value consignments move by secure road convoy, approved air freight and '
                    'international ferry routes — always under GPS monitoring and documented custody. '
                    'Multi-modal transfers are conducted in secure transit hubs with CCTV coverage, '
                    'ensuring unbroken protection from origin to final destination.'
                ),
                'highlights': [
                    'GPS-monitored armored road transport and secure convoy protocols',
                    'Approved air freight with airside secure handover procedures',
                    'International routing via vetted logistics partners',
                    'CCTV-covered secure transit hubs for multi-modal transfers',
                ],
                'image': 'services/precious-goods-transport/detail-2.png',
                'reverse': True,
            },
        ],
        'gallery': [],
        'clients_heading': 'Items Transported',
        'clients': [
            'Gold, silver and precious metal bullion',
            'Diamonds, gemstones and finished jewellery',
            'Luxury watches and horological collectibles',
            'Fine art, antiques and museum pieces',
            'Rare collectibles and luxury fashion items',
            'Confidential high-value commercial goods',
        ],
        'features_heading': 'Security Measures Include',
        'features': [
            'Pre-movement route and threat risk assessment',
            'Specialist tamper-evident packaging by asset type',
            'Real-time GPS tracking and 24/7 control-room monitoring',
            'Secure routing with approved multi-modal transfer points',
            'Full chain-of-custody documentation at every handover',
            'Insured carriage with per-consignment certificates',
            'Optional armed escort (subject to jurisdiction and assessment)',
            'Customs facilitation for international movements',
        ],
    },
    'payment-digital-services': {
        'title': 'Payment & Digital Services',
        'tagline': 'Encrypted payment platforms, real-time cash dashboards and GPS-linked shipment visibility.',
        'hero_image': 'services/payment-digital-services/hero.png',
        'premium': True,
        'what_it_means': (
            'Payment and Digital Services bridge physical cash logistics with secure digital financial '
            'tools — giving businesses full visibility and control over payments, reporting and cash '
            'position across every site. Encrypted client portals connect field operations, armored '
            'transport and treasury teams in real time — with GPS-linked consignment tracking, '
            'automated deposit reporting and business analytics built on tamper-proof data feeds.'
        ),
        'overview_points': [
            'Encrypted client portals with role-based access controls',
            'Real-time GPS-linked tracking of all physical consignments',
            'Automated cash reporting dashboards for multi-site operations',
            'Secure digital payment processing integrated with physical logistics',
        ],
        'security_protocols': [
            {
                'title': 'Encrypted Client Portals',
                'text': (
                    'All digital services are accessed through TLS-encrypted client portals protected '
                    'by multi-factor authentication and role-based access controls. Session activity '
                    'is logged, and privileged actions — such as authorising high-value movements — '
                    'require dual approval from designated client administrators.'
                ),
            },
            {
                'title': 'GPS-Linked Consignment Tracking',
                'text': (
                    'Physical consignments are linked to live GPS telemetry on our digital platform. '
                    'Authorised users see real-time location, estimated arrival and custody status — '
                    'with automated notifications at key milestones including collection, transit hub '
                    'arrival and verified delivery.'
                ),
            },
            {
                'title': 'Automated Reporting & Reconciliation',
                'text': (
                    'Cash reporting dashboards aggregate data from field collections, processing centres '
                    'and deposit confirmations into a single treasury view. Reports are generated from '
                    'tamper-proof system logs — not manual entry — ensuring accuracy for audit, '
                    'regulatory compliance and internal reconciliation.'
                ),
            },
            {
                'title': 'Secure Payment Processing',
                'text': (
                    'Digital payment processing is integrated with our physical cash logistics network, '
                    'enabling seamless settlement between armored collection, vault storage and bank '
                    'deposit. All transactions are encrypted, logged and available for export to your '
                    'ERP or accounting systems via secure API.'
                ),
            },
        ],
        'editorial_blocks': [
            {
                'title': 'Digital Payment & Reporting Platforms',
                'body': (
                    'Treasury and finance teams access a unified dashboard showing cash position, '
                    'pending collections, in-transit consignments and completed deposits across every '
                    'site. Electronic invoicing, deposit reporting and account management tools reduce '
                    'manual reconciliation and give leadership real-time visibility over physical cash flows.'
                ),
                'highlights': [
                    'Multi-site cash position dashboard updated in real time',
                    'Automated deposit and collection reporting',
                    'Electronic invoicing linked to physical service records',
                    'Role-based portal access with multi-factor authentication',
                ],
                'image': 'services/payment-digital-services/detail-1.png',
                'reverse': False,
            },
            {
                'title': 'Integrated Cash Intelligence & Analytics',
                'body': (
                    'Our digital layer connects armored field operations to your finance team — '
                    'eliminating the delays and discrepancies that arise when physical and digital '
                    'records are maintained separately. Business analytics tools identify trends in '
                    'cash volume, collection frequency and float requirements across your estate.'
                ),
                'highlights': [
                    'GPS-linked live tracking of all consignments on one platform',
                    'Business analytics for cash volume and float optimisation',
                    'Secure API integration with ERP and accounting systems',
                    'Tamper-proof audit logs for regulatory compliance',
                ],
                'image': 'services/payment-digital-services/detail-2.png',
                'reverse': True,
            },
        ],
        'gallery': [],
        'clients_heading': '',
        'clients': [],
        'features_heading': 'Examples Include',
        'features': [
            'Encrypted digital payment processing and settlement',
            'Real-time cash reporting dashboards for treasury teams',
            'GPS-linked online consignment and shipment tracking',
            'Electronic invoicing tied to physical service records',
            'Automated deposit reporting with tamper-proof data feeds',
            'Secure account management portals with MFA access',
            'Business analytics for cash-flow and float optimisation',
            'Secure API integration with ERP and accounting platforms',
        ],
    },
    'risk-special-operations': {
        'title': 'Risk & Special Operations',
        'tagline': 'Threat-assessed escort, emergency logistics and bespoke security planning for high-risk assignments.',
        'hero_image': 'services/risk-special-operations/hero.png',
        'premium': True,
        'what_it_means': (
            'Risk and Special Operations deliver customised security and logistics solutions for '
            'complex, sensitive or high-risk assignments that exceed standard service parameters. '
            'Every mission begins with a formal threat and route assessment, followed by bespoke '
            'planning, GPS-monitored execution and post-operation audit reporting — covering large '
            'cash movements, event security, emergency logistics, election support and disaster-response '
            'asset transport.'
        ),
        'overview_points': [
            'Formal threat and route assessment before every mission is authorised',
            'Bespoke security plans approved by senior operations leadership',
            'GPS-monitored execution with dedicated control-room oversight',
            'Post-operation audit reports for client and regulatory review',
        ],
        'security_protocols': [
            {
                'title': 'Threat & Route Assessment',
                'text': (
                    'No special operation commences without a documented threat assessment covering '
                    'political climate, criminal intelligence, route geography, timing and asset value. '
                    'Assessments are reviewed by senior security leadership and approved before resources '
                    'are deployed — with contingency routes and fallback protocols pre-planned.'
                ),
            },
            {
                'title': 'Bespoke Mission Planning',
                'text': (
                    'Each assignment receives a dedicated mission plan specifying personnel, vehicles, '
                    'communications, escalation procedures and rendezvous points. Plans are distributed '
                    'only to authorised mission personnel on encrypted channels and are never shared '
                    'outside the operational team.'
                ),
            },
            {
                'title': 'GPS-Monitored Execution & Escort',
                'text': (
                    'Mission vehicles operate under real-time GPS tracking with a dedicated control-room '
                    'supervisor assigned to each operation. Armed escort teams maintain continuous '
                    'communication with the control room and follow pre-approved engagement protocols '
                    'appropriate to jurisdiction and threat level.'
                ),
            },
            {
                'title': 'Post-Operation Audit & Reporting',
                'text': (
                    'Every completed mission generates a post-operation report documenting timeline, '
                    'personnel, route adherence, incidents and custody handovers. Reports are delivered '
                    'securely to the client within agreed timeframes and are retained for regulatory '
                    'and insurance audit purposes.'
                ),
            },
        ],
        'editorial_blocks': [
            {
                'title': 'Special Operations & Tactical Response',
                'body': (
                    'When standard logistics protocols are insufficient, our special operations teams '
                    'deploy with advanced security capabilities — including tactical escort, secure '
                    'breaching support for emergency access and rapid-response asset recovery. Every '
                    'deployment is governed by a written mission plan approved at senior leadership level.'
                ),
                'highlights': [
                    'Tactical escort teams with jurisdiction-appropriate authorisation',
                    'Emergency access and secure breaching support where required',
                    'Rapid-response asset recovery and relocation capability',
                    'Encrypted communications and dedicated mission control channel',
                ],
                'image': 'services/risk-special-operations/detail-1.png',
                'reverse': False,
            },
            {
                'title': 'Emergency Logistics & Command Coordination',
                'body': (
                    'From disaster-response asset transport to election logistics and large-scale event '
                    'cash management, our operations centre coordinates multi-agency missions with '
                    'mobile command capability. GPS-tracked convoys, emergency management officers and '
                    'senior project planners ensure complex assignments are executed safely and on schedule.'
                ),
                'highlights': [
                    'Mobile command units for large-scale and emergency operations',
                    'Multi-agency coordination with law enforcement and government bodies',
                    'GPS-tracked convoy management for large cash and asset movements',
                    'Dedicated emergency management officers on critical assignments',
                ],
                'image': 'services/risk-special-operations/detail-2.png',
                'reverse': True,
            },
        ],
        'gallery': [],
        'clients_heading': '',
        'clients': [],
        'features_heading': 'Examples Include',
        'features': [
            'Large-scale cash and asset movements with armed escort',
            'Event cash management and on-site security coordination',
            'Emergency logistics and disaster-response asset transport',
            'Election logistics support and secure ballot handling',
            'High-security project planning and mission documentation',
            'Security consulting and independent threat assessments',
            'Route planning with GPS-monitored convoy execution',
            'Post-operation audit reporting for compliance and insurance',
        ],
    },
}


def get_service(slug):
    return SERVICES.get(slug)


def all_services():
    return SERVICES
