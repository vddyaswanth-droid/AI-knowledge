"""
AutoSage Knowledge Base
Comprehensive automotive symptom definitions, subsystem mappings,
diagnostic combination rules, pre-mechanic checklists, and mechanic guide.
"""

# Subsystems monitored by AutoSage
SUBSYSTEMS = {
    "powertrain": {
        "name": "Engine & Powertrain",
        "description": "Internal combustion, engine cooling, lubrication, and core power generation.",
        "icon": "⚡"
    },
    "transmission": {
        "name": "Transmission & Driveline",
        "description": "Gearbox, clutch/torque converter, drive axles, and differential.",
        "icon": "⚙️"
    },
    "brakes": {
        "name": "Brakes & Safety",
        "description": "Pads, rotors, calipers, hydraulic brake lines, master cylinder, and ABS.",
        "icon": "🛑"
    },
    "suspension": {
        "name": "Suspension & Steering",
        "description": "Struts, shock absorbers, control arms, tie rods, wheel bearings, and alignment.",
        "icon": "🛞"
    },
    "electrical": {
        "name": "Electrical & Starting",
        "description": "12V battery, alternator, starter motor, ignition coils, and wiring.",
        "icon": "🔋"
    },
    "emissions_fuel": {
        "name": "Fuel & Emissions",
        "description": "Fuel injectors, fuel pump, catalytic converter, O2 sensors, and EVAP.",
        "icon": "⛽"
    }
}

# Master Symptom Catalog
SYMPTOMS = {
    # --- Engine & Cooling ---
    "engine_overheating": {
        "id": "engine_overheating",
        "title": "Engine Overheating",
        "category": "Engine & Cooling",
        "subsystem": "powertrain",
        "description": "Temperature gauge needle creeps into the red zone, or coolant boiling steam escapes from hood.",
        "base_severity": "high",
        "icon": "🔥"
    },
    "sweet_syrup_smell": {
        "id": "sweet_syrup_smell",
        "title": "Sweet Maple Syrup Smell",
        "category": "Engine & Cooling",
        "subsystem": "powertrain",
        "description": "Noticeable sweet pancake syrup odor through A/C vents or around the front grill.",
        "base_severity": "moderate",
        "icon": "🥞"
    },
    "white_exhaust_smoke": {
        "id": "white_exhaust_smoke",
        "title": "Thick White Exhaust Smoke",
        "category": "Engine & Cooling",
        "subsystem": "powertrain",
        "description": "Persistent billowy white vapor trailing behind vehicle even after the car is warm.",
        "base_severity": "high",
        "icon": "💨"
    },
    "engine_rough_idle": {
        "id": "engine_rough_idle",
        "title": "Rough or Shaking Idle",
        "category": "Engine & Cooling",
        "subsystem": "powertrain",
        "description": "Car shakes, stumbles, or RPM tachometer needle bounces erratically when stopped in gear.",
        "base_severity": "moderate",
        "icon": "📳"
    },
    "engine_stalling": {
        "id": "engine_stalling",
        "title": "Engine Stalls or Dies Unexpectedly",
        "category": "Engine & Cooling",
        "subsystem": "powertrain",
        "description": "Engine shuts off unexpectedly when slowing down, idling at stoplights, or after starting.",
        "base_severity": "high",
        "icon": "⚠️"
    },
    "engine_knocking_sound": {
        "id": "engine_knocking_sound",
        "title": "Deep Metallic Knocking Sound",
        "category": "Engine & Cooling",
        "subsystem": "powertrain",
        "description": "Rhythmic metallic clatter or deep rapping from lower engine block that speeds up with RPM.",
        "base_severity": "critical",
        "icon": "🔨"
    },
    "ticking_valve_sound": {
        "id": "ticking_valve_sound",
        "title": "Fast Ticking or Chattering Sound",
        "category": "Engine & Cooling",
        "subsystem": "powertrain",
        "description": "Rapid sewing-machine-like clicking noise from the top of the engine, often loudest on cold start.",
        "base_severity": "moderate",
        "icon": "⏱️"
    },
    "oil_puddle_under_car": {
        "id": "oil_puddle_under_car",
        "title": "Dark Brown or Amber Fluid Puddle",
        "category": "Engine & Cooling",
        "subsystem": "powertrain",
        "description": "Slippery, dark amber to black fluid pool beneath the front engine area when parked.",
        "base_severity": "moderate",
        "icon": "🛢️"
    },
    "low_oil_pressure_light": {
        "id": "low_oil_pressure_light",
        "title": "Red Oil Can Light on Dash",
        "category": "Engine & Cooling",
        "subsystem": "powertrain",
        "description": "Red oil dripping can symbol illuminated while engine is running.",
        "base_severity": "critical",
        "icon": "🚨"
    },

    # --- Transmission & Driveline ---
    "transmission_slipping": {
        "id": "transmission_slipping",
        "title": "Transmission Slipping",
        "category": "Transmission & Driveline",
        "subsystem": "transmission",
        "description": "Engine revs up loudly but the vehicle doesn't speed up proportionally, like it's in neutral.",
        "base_severity": "high",
        "icon": "🔄"
    },
    "delayed_gear_engagement": {
        "id": "delayed_gear_engagement",
        "title": "Delayed Engagement (Lag into Drive/Reverse)",
        "category": "Transmission & Driveline",
        "subsystem": "transmission",
        "description": "Pauses for 1-3 seconds after shifting from Park into Drive or Reverse before engaging with a thump.",
        "base_severity": "moderate",
        "icon": "⏳"
    },
    "rough_hard_shifting": {
        "id": "rough_hard_shifting",
        "title": "Harsh or Clunking Gear Shifts",
        "category": "Transmission & Driveline",
        "subsystem": "transmission",
        "description": "Car jerks or jolts abruptly when transitioning gears while accelerating.",
        "base_severity": "moderate",
        "icon": "💥"
    },
    "red_fluid_leak": {
        "id": "red_fluid_leak",
        "title": "Pink or Bright Red Fluid Leak",
        "category": "Transmission & Driveline",
        "subsystem": "transmission",
        "description": "Reddish, slightly oily fluid dripping underneath the center of the engine or chassis.",
        "base_severity": "high",
        "icon": "🩸"
    },
    "transmission_burning_smell": {
        "id": "transmission_burning_smell",
        "title": "Burnt Tart / Acrid Odor",
        "category": "Transmission & Driveline",
        "subsystem": "transmission",
        "description": "Hot, burnt toast or acrid chemical smell after driving, especially after uphill climbing.",
        "base_severity": "high",
        "icon": "♨️"
    },

    # --- Brakes & Stopping ---
    "brake_squealing": {
        "id": "brake_squealing",
        "title": "High-Pitched Squeal When Braking",
        "category": "Brakes & Stopping",
        "subsystem": "brakes",
        "description": "Piercing metallic squeal when pressing the brake pedal, usually stops when releasing.",
        "base_severity": "moderate",
        "icon": "🎺"
    },
    "brake_grinding_noise": {
        "id": "brake_grinding_noise",
        "title": "Harsh Metal-on-Metal Grinding Sound",
        "category": "Brakes & Stopping",
        "subsystem": "brakes",
        "description": "Gruff scratching or grinding noise like metal dragging against asphalt during braking.",
        "base_severity": "critical",
        "icon": "⚔️"
    },
    "spongy_soft_brake_pedal": {
        "id": "spongy_soft_brake_pedal",
        "title": "Spongy, Soft, or Sinking Brake Pedal",
        "category": "Brakes & Stopping",
        "subsystem": "brakes",
        "description": "Brake pedal feels squishy and travels unusually close to the floorboard before stopping the car.",
        "base_severity": "critical",
        "icon": "🧽"
    },
    "brake_pulsation_vibration": {
        "id": "brake_pulsation_vibration",
        "title": "Pulsating Pedal / Steering Shake While Braking",
        "category": "Brakes & Stopping",
        "subsystem": "brakes",
        "description": "Brake pedal rhythmically pulses underfoot or steering wheel shivers when slowing down from speed.",
        "base_severity": "moderate",
        "icon": "〰️"
    },
    "car_pulls_when_braking": {
        "id": "car_pulls_when_braking",
        "title": "Car Pulls to One Side When Braking",
        "category": "Brakes & Stopping",
        "subsystem": "brakes",
        "description": "Vehicle veers noticeably to the left or right whenever the brakes are pressed.",
        "base_severity": "high",
        "icon": "↔️"
    },
    "brake_warning_light": {
        "id": "brake_warning_light",
        "title": "Red Brake Light or ABS Light On",
        "category": "Brakes & Stopping",
        "subsystem": "brakes",
        "description": "Dashboard parking brake light stays illuminated while driving or amber 'ABS' icon is active.",
        "base_severity": "high",
        "icon": "⚠️"
    },

    # --- Suspension, Steering & Wheels ---
    "highway_vibration": {
        "id": "highway_vibration",
        "title": "Vibration at Highway Speeds (50-70 mph / 80-110 km/h)",
        "category": "Suspension & Steering",
        "subsystem": "suspension",
        "description": "Steering wheel or entire car seat buzzes or oscillates when cruising at highway speeds.",
        "base_severity": "moderate",
        "icon": "📳"
    },
    "steering_pulls_straight_road": {
        "id": "steering_pulls_straight_road",
        "title": "Car Drifts/Pulls on Flat Road",
        "category": "Suspension & Steering",
        "subsystem": "suspension",
        "description": "Car continually wanders toward the ditch or lane lines when driving on level pavement without braking.",
        "base_severity": "low",
        "icon": "↖️"
    },
    "clunking_over_bumps": {
        "id": "clunking_over_bumps",
        "title": "Dull Clunk or Thumping Over Potholes/Bumps",
        "category": "Suspension & Steering",
        "subsystem": "suspension",
        "description": "Heavy hollow knocking sound from under the wheels when rolling over bumps or driveway ramps.",
        "base_severity": "moderate",
        "icon": "🪨"
    },
    "squeaking_over_bumps": {
        "id": "squeaking_over_bumps",
        "title": "High-Pitched Creaking/Squeaking Over Dips",
        "category": "Suspension & Steering",
        "subsystem": "suspension",
        "description": "Old mattress-like squeaking when the car body rocks, bounces, or enters speed humps.",
        "base_severity": "low",
        "icon": "🐁"
    },
    "heavy_stiff_steering": {
        "id": "heavy_stiff_steering",
        "title": "Heavy, Hard-to-Turn Steering Wheel",
        "category": "Suspension & Steering",
        "subsystem": "suspension",
        "description": "Requires significant physical effort to turn the wheel during parking or low-speed maneuvers.",
        "base_severity": "high",
        "icon": "💪"
    },
    "uneven_tire_wear": {
        "id": "uneven_tire_wear",
        "title": "Uneven Tire Tread Wear",
        "category": "Suspension & Steering",
        "subsystem": "suspension",
        "description": "Inner or outer edge of the tire tread is worn flat while the other side still has deep grooves.",
        "base_severity": "moderate",
        "icon": "⭕"
    },

    # --- Electrical & Starting ---
    "clicking_when_starting": {
        "id": "clicking_when_starting",
        "title": "Rapid Clicking When Turning Key / Push Start",
        "category": "Electrical & Starting",
        "subsystem": "electrical",
        "description": "Rapid machine-gun click-click-click noise when trying to start, but the engine won't turn over.",
        "base_severity": "moderate",
        "icon": "🔌"
    },
    "slow_engine_crank": {
        "id": "slow_engine_crank",
        "title": "Sluggish / Labored Engine Crank",
        "category": "Electrical & Starting",
        "subsystem": "electrical",
        "description": "Engine groans sluggishly (rur... rur... rur...) before catching, especially on cold mornings.",
        "base_severity": "moderate",
        "icon": "🐢"
    },
    "no_crank_no_start": {
        "id": "no_crank_no_start",
        "title": "Completely Dead - No Crank, No Dash Lights",
        "category": "Electrical & Starting",
        "subsystem": "electrical",
        "description": "Turning the key or pressing start does nothing; interior lights and dashboard stay completely dark.",
        "base_severity": "high",
        "icon": "🪫"
    },
    "dim_flickering_lights": {
        "id": "dim_flickering_lights",
        "title": "Dim or Flickering Headlights / Dash Lights",
        "category": "Electrical & Starting",
        "subsystem": "electrical",
        "description": "Lights dim noticeably at idle and brighten up when you press the gas pedal.",
        "base_severity": "moderate",
        "icon": "💡"
    },
    "battery_warning_light": {
        "id": "battery_warning_light",
        "title": "Battery Icon Light While Driving",
        "category": "Electrical & Starting",
        "subsystem": "electrical",
        "description": "Red battery outline symbol appears on the dashboard while driving down the road.",
        "base_severity": "high",
        "icon": "🪫"
    },

    # --- Fuel, Air & Emissions ---
    "reduced_fuel_economy": {
        "id": "reduced_fuel_economy",
        "title": "Sudden Drop in Fuel Efficiency (MPG / km/L)",
        "category": "Fuel & Emissions",
        "subsystem": "emissions_fuel",
        "description": "Getting significantly fewer miles per tank of gas than usual without changes in driving habits.",
        "base_severity": "low",
        "icon": "📉"
    },
    "sluggish_acceleration": {
        "id": "sluggish_acceleration",
        "title": "Sluggish Acceleration / Hesitation",
        "category": "Fuel & Emissions",
        "subsystem": "emissions_fuel",
        "description": "Car feels choked, bogs down, or hesitates when stepping on the gas pedal to pass or merge.",
        "base_severity": "moderate",
        "icon": "🐌"
    },
    "black_exhaust_smoke": {
        "id": "black_exhaust_smoke",
        "title": "Black Sooty Exhaust Smoke",
        "category": "Fuel & Emissions",
        "subsystem": "emissions_fuel",
        "description": "Dark black smoke puffs out the tailpipe, leaving black soot residue around the exhaust tip.",
        "base_severity": "moderate",
        "icon": "🖤"
    },
    "blue_exhaust_smoke": {
        "id": "blue_exhaust_smoke",
        "title": "Bluish-Gray Exhaust Smoke",
        "category": "Fuel & Emissions",
        "subsystem": "emissions_fuel",
        "description": "Bluish smoke with an oily burning odor coming from the exhaust pipe, especially when accelerating.",
        "base_severity": "high",
        "icon": "🫐"
    },
    "rotten_egg_sulfur_smell": {
        "id": "rotten_egg_sulfur_smell",
        "title": "Rotten Egg / Strong Sulfur Odor",
        "category": "Fuel & Emissions",
        "subsystem": "emissions_fuel",
        "description": "Pungent rotten egg stink coming from the rear exhaust or inside the cabin during driving.",
        "base_severity": "moderate",
        "icon": "🥚"
    },
    "check_engine_light_steady": {
        "id": "check_engine_light_steady",
        "title": "Steady (Solid) Check Engine Light",
        "category": "Fuel & Emissions",
        "subsystem": "emissions_fuel",
        "description": "Amber or yellow engine symbol stays lit continuously on the gauge cluster.",
        "base_severity": "moderate",
        "icon": "🟡"
    },
    "check_engine_light_flashing": {
        "id": "check_engine_light_flashing",
        "title": "Flashing / Blinking Check Engine Light",
        "category": "Fuel & Emissions",
        "subsystem": "emissions_fuel",
        "description": "Amber engine icon is repeatedly blinking or flashing while the engine is running.",
        "base_severity": "critical",
        "icon": "🚨"
    }
}

# Combination Rules Matrix
# Evaluated in priority order: complex multi-symptom matches first, then specific dual matches.
DIAGNOSTIC_RULES = [
    {
        "id": "RULE_CRIT_HEAD_GASKET",
        "match_type": "all",
        "required_symptoms": ["engine_overheating", "white_exhaust_smoke"],
        "optional_symptoms": ["sweet_syrup_smell", "engine_rough_idle"],
        "min_score": 95,
        "urgency": "critical",
        "urgency_label": "CRITICAL: Do Not Drive",
        "title": "Blown Cylinder Head Gasket / Coolant Breach",
        "subsystem_impacts": {"powertrain": 75, "emissions_fuel": 30},
        "explanation": "Thick white sweet-smelling exhaust smoke coupled with engine overheating is a classic hallmark of coolant entering the engine combustion cylinders. The cylinder head gasket has likely ruptured, allowing pressurized coolant to vaporize in the cylinders and hot exhaust gasses to over-pressurize the cooling jacket.",
        "risk_explanation": "Driving even a few miles with a blown head gasket can warp the aluminum engine cylinder head, contaminate motor oil with coolant (turning it into a milky sludge that destroys rod bearings), or cause total engine seizure requiring a multi-thousand-dollar replacement.",
        "diy_checks": [
            "Wait until engine is 100% ice cold (minimum 2 hours). Pull the engine oil dipstick: inspect if the oil appears like chocolate milk or creamy coffee instead of golden amber/brown.",
            "Remove the oil filler cap under the hood: check if there is thick white/yellow mayonnaise-like foam on the underside of the cap.",
            "NEVER open the radiator cap when the engine is warm. When fully cold, check if the coolant level in the expansion tank is bubbling or mysteriously bone dry."
        ],
        "mechanic_questions": [
            "Can you perform a chemical combustion gas block test (liquid sniff test) on the radiator?",
            "Will you perform a cylinder leak-down test to confirm which cylinder has the gasket breach?",
            "If the head gasket has failed, does your estimate include checking and machining the cylinder head for warping or cracks?"
        ],
        "estimated_cost_tier": "Major ($1,200 - $2,800 depending on vehicle make and labor rates)"
    },
    {
        "id": "RULE_CRIT_FLASHING_CEL",
        "match_type": "all",
        "required_symptoms": ["check_engine_light_flashing"],
        "optional_symptoms": ["engine_rough_idle", "sluggish_acceleration", "reduced_fuel_economy"],
        "min_score": 96,
        "urgency": "critical",
        "urgency_label": "CRITICAL: Stop Driving Immediately",
        "title": "Active Severe Cylinder Misfire (Catalytic Converter Danger)",
        "subsystem_impacts": {"powertrain": 70, "emissions_fuel": 65},
        "explanation": "A blinking or flashing Check Engine Light is universal automotive code for an ACTIVE severe cylinder misfire. One or more cylinders are failing to ignite the air-fuel mixture, causing raw, unburned gasoline to be pumped straight down the exhaust manifold.",
        "risk_explanation": "Raw gasoline ignites inside the honeycomb core of your catalytic converter, heating it to over 1,800°F (1,000°C). This can melt the catalytic converter into a solid block within 15 minutes of driving, and in severe cases poses a vehicle undercarriage fire hazard.",
        "diy_checks": [
            "Pull over safely as soon as possible and shut off the engine.",
            "Under the hood, check if any ignition coil wire harnesses are visibly chewed by rodents or unplugged.",
            "Do not drive on highways or at high RPM. Arrange a tow or limp very gently to the closest repair facility if within 1 mile."
        ],
        "mechanic_questions": [
            "Which specific cylinder fault codes (P0300, P0301-P0308) are stored in the ECU freeze-frame data?",
            "Is the misfire caused by a failed ignition coil, fouled spark plug, or a stuck fuel injector?",
            "Can you verify catalytic converter inlet temperature and backpressure to confirm it did not melt?"
        ],
        "estimated_cost_tier": "Minor to Moderate ($150 - $450 if spark plug/ignition coil; $1,000+ if catalytic converter was damaged)"
    },
    {
        "id": "RULE_CRIT_BRAKE_GRIND",
        "match_type": "all",
        "required_symptoms": ["brake_grinding_noise"],
        "optional_symptoms": ["spongy_soft_brake_pedal", "brake_pulsation_vibration", "car_pulls_when_braking"],
        "min_score": 92,
        "urgency": "critical",
        "urgency_label": "CRITICAL: Unsafe to Drive",
        "title": "Complete Friction Material Exhaustion (Metal-on-Metal Braking)",
        "subsystem_impacts": {"brakes": 85},
        "explanation": "Harsh metallic grinding sound when stepping on the brakes indicates that the friction brake pad compound has worn down completely to zero, and the steel backing plate is now gouging directly into the iron brake rotor disc.",
        "risk_explanation": "Stopping distances are drastically multiplied. Severe friction heat can cause the brake caliper piston to over-extend, boil the brake fluid (causing total hydraulic brake failure), or score the rotors so deeply that they can crack or seize.",
        "diy_checks": [
            "Look through the wheel spokes with a flashlight: inspect the shiny surface of the brake rotor disc for deep circular grooves or metal shavings on the rim.",
            "Check the brake fluid reservoir level in the engine bay: severely worn pads often pull the fluid level down near the MIN line."
        ],
        "mechanic_questions": [
            "Are both brake pads and rotors required on this axle, or can the rotors be resurfaced (turned)?",
            "Has the caliper piston seal or dust boot been heat-damaged from metal friction?",
            "What is the remaining friction percentage on the opposite axle?"
        ],
        "estimated_cost_tier": "Moderate ($250 - $600 per axle for pads and premium rotors)"
    },
    {
        "id": "RULE_CRIT_LOW_OIL_PRESSURE",
        "match_type": "all",
        "required_symptoms": ["low_oil_pressure_light"],
        "optional_symptoms": ["ticking_valve_sound", "engine_knocking_sound", "oil_puddle_under_car"],
        "min_score": 98,
        "urgency": "critical",
        "urgency_label": "CRITICAL: Engine Seizure Imminent",
        "title": "Loss of Engine Lubrication Pressure",
        "subsystem_impacts": {"powertrain": 90},
        "explanation": "The red oil pressure warning light indicates that engine oil pressure has plummeted below the safe threshold (often under 5-7 PSI). It does not just mean low oil level—it means moving crankshaft journals and camshafts are metal-on-metal without hydrodynamic oil cushioning.",
        "risk_explanation": "An engine running with low oil pressure can suffer spun rod bearings or total catastrophic lockup within seconds to minutes of driving.",
        "diy_checks": [
            "Turn off the engine immediately. Do not attempt to drive to a shop.",
            "Wait 5 minutes for oil to settle, pull the oil dipstick, wipe it clean with a rag, reinsert fully, and pull again: check if oil level is between MIN and MAX marks.",
            "If bone dry, adding 1-2 quarts of matching viscosity oil may restore pressure if there's no major hole in the oil pan."
        ],
        "mechanic_questions": [
            "Can you test mechanical oil pressure with an external master oil gauge?",
            "Is the failure due to an oil pump failure, clogged oil pickup tube screen, or a faulty oil pressure sending unit switch?",
            "Did internal engine bearings sustain scoring damage?"
        ],
        "estimated_cost_tier": "Moderate to Extreme ($150 for sensor replacement; $800 - $3,500 if pump or bearings failed)"
    },
    {
        "id": "RULE_HIGH_WARPED_ROTORS",
        "match_type": "all",
        "required_symptoms": ["brake_pulsation_vibration"],
        "optional_symptoms": ["brake_squealing", "highway_vibration"],
        "min_score": 75,
        "urgency": "high",
        "urgency_label": "HIGH: Inspect Soon",
        "title": "Brake Rotor Thickness Variation / Warped Rotors",
        "subsystem_impacts": {"brakes": 60, "suspension": 20},
        "explanation": "If vibration or steering shake occurs ONLY or PRIMARILY when stepping on the brakes, the brake rotor discs have developed thickness variation (runout) or uneven brake pad material transfer. As the caliper clamps down on the spinning rotor, the uneven surfaces kick back against the hydraulic pistons.",
        "risk_explanation": "Reduces emergency braking effectiveness, creates uneven pad wear, and excessive vibration puts premature stress on steering tie-rod ends and wheel hub bearings.",
        "diy_checks": [
            "Verify if the shake is felt through the steering wheel (indicates FRONT rotors) or through your seat/brake pedal (indicates REAR rotors).",
            "Notice if the pulsation is worse when stopping from high speeds on highway off-ramps.",
            "Inspect wheel rims for excessive dark brake dust on one wheel compared to the others."
        ],
        "mechanic_questions": [
            "Can you measure the rotor runout with a dial indicator?",
            "Do the rotors have enough thickness remaining to be resurfaced (turned) on an on-car brake lathe?",
            "Are the caliper slide pins moving freely or are they sticking and causing uneven heat buildup?"
        ],
        "estimated_cost_tier": "Moderate ($200 - $450 for front or rear brake service)"
    },
    {
        "id": "RULE_HIGH_TRANSMISSION_LEAK",
        "match_type": "any",
        "required_symptoms": ["transmission_slipping", "red_fluid_leak"],
        "optional_symptoms": ["delayed_gear_engagement", "rough_hard_shifting", "transmission_burning_smell"],
        "min_score": 85,
        "urgency": "high",
        "urgency_label": "HIGH: Service Urgently",
        "title": "Low Transmission Fluid / Internal Hydraulic Slippage",
        "subsystem_impacts": {"transmission": 75},
        "explanation": "Automatic transmissions rely entirely on hydraulic fluid pressure to clamp clutch packs together and lubricate planet gears. If transmission fluid has leaked or broken down thermally, the clutch plates cannot lock firmly, causing high engine revs without vehicle momentum.",
        "risk_explanation": "Operating an automatic or CVT transmission while slipping causes friction clutch material to glaze, crumble, and burn within days. Replacing low fluid early saves you from a $3,500+ transmission rebuild.",
        "diy_checks": [
            "If your vehicle has a transmission dipstick (often yellow or red loop near firewall): check fluid with engine warm and idling in Park on flat ground.",
            "Wipe dipstick on a white paper towel: healthy fluid is translucent bright pink/red. Dark brown/black fluid with a burnt smell indicates severe clutch wear.",
            "Check for reddish oily stains on your parking spot or garage floor."
        ],
        "mechanic_questions": [
            "Where is the transmission fluid leaking from (cooler lines, pan gasket, axle seals, or torque converter seal)?",
            "What condition is the drained fluid in—is there metal flake or clutch sediment in the pan magnet?",
            "Will a pan drop, new filter, and fluid drain-and-fill resolve the issue without a full overhaul?"
        ],
        "estimated_cost_tier": "Moderate ($180 - $400 for leak repair and fluid service; $2,500 - $4,500 if internal clutches are burned)"
    },
    {
        "id": "RULE_HIGH_ALTERNATOR_FAILURE",
        "match_type": "all",
        "required_symptoms": ["battery_warning_light"],
        "optional_symptoms": ["dim_flickering_lights", "slow_engine_crank", "clicking_when_starting"],
        "min_score": 82,
        "urgency": "high",
        "urgency_label": "HIGH: Immediate Breakdown Risk",
        "title": "Charging System / Alternator Failure",
        "subsystem_impacts": {"electrical": 75},
        "explanation": "The red battery icon does NOT mean your battery is dead—it warns that the alternator is NOT producing sufficient voltage (13.8V - 14.5V) to charge the battery while the engine runs. The car is running on reserve battery power alone.",
        "risk_explanation": "A vehicle running solely on battery power will run for only 15 to 45 minutes before the battery drops below 10.5V, causing the engine computer, electric power steering, fuel pump, and lights to shut off suddenly in traffic.",
        "diy_checks": [
            "Check under the hood for a loose, squealing, or snapped serpentine accessory drive belt.",
            "Inspect the battery terminals for fuzzy blue/white corrosion crust or loose terminal clamps that wiggle by hand.",
            "Turn off all non-essential electrical accessories (A/C, seat heaters, radio, headlights if daytime) to maximize reserve battery distance."
        ],
        "mechanic_questions": [
            "What is the alternator output voltage and amperage under electrical load test?",
            "Is the serpentine belt tensioner worn or slipping?",
            "Has the battery sustained deep-cycle discharge damage that requires replacement as well?"
        ],
        "estimated_cost_tier": "Moderate ($350 - $700 for alternator replacement and labor)"
    },
    {
        "id": "RULE_HIGH_OVERHEATING_FAN",
        "match_type": "all",
        "required_symptoms": ["engine_overheating"],
        "optional_symptoms": ["sweet_syrup_smell", "engine_rough_idle"],
        "min_score": 78,
        "urgency": "high",
        "urgency_label": "HIGH: Stop Driving if Gauge Rises",
        "title": "Cooling System Failure (Radiator Fan / Thermostat / Water Pump)",
        "subsystem_impacts": {"powertrain": 65},
        "explanation": "Engine overheating occurs when heat generated by combustion cannot be dissipated into the atmosphere. Common causes include a stuck-closed thermostat, inoperative electric radiator cooling fan, leaking radiator hose, or failing water pump impeller.",
        "risk_explanation": "Continuing to drive an overheating engine will warp aluminum cylinder heads, blow head gaskets, and cause internal piston scuffing.",
        "diy_checks": [
            "CRITICAL: NEVER remove the radiator pressure cap when the engine is hot! Scalding steam and pressurized boiling coolant will cause severe burns.",
            "Turn your cabin heater to full blast and highest heat setting—this acts as a secondary mini-radiator and can pull excess heat off the engine.",
            "When the engine is running and hot, look through the front grill: is the radiator electric cooling fan spinning vigorously?",
            "Inspect under the front bumper for bright neon green, pink, or orange liquid dripping onto the pavement."
        ],
        "mechanic_questions": [
            "Can you perform a cooling system pressure test to pinpoint any external or internal leaks?",
            "Is the electric cooling fan motor and relay receiving 12V power?",
            "Is the thermostat opening fully at its rated temperature (around 195°F / 90°C)?"
        ],
        "estimated_cost_tier": "Moderate ($150 - $450 for thermostat/hose/fan relay; $400 - $850 for water pump or radiator)"
    },
    {
        "id": "RULE_MOD_WHEEL_UNBALANCE",
        "match_type": "all",
        "required_symptoms": ["highway_vibration"],
        "optional_symptoms": ["steering_pulls_straight_road", "uneven_tire_wear"],
        "min_score": 60,
        "urgency": "moderate",
        "urgency_label": "MODERATE: Schedule Inspection",
        "title": "Wheel Out-of-Balance or Tire Radial Runout",
        "subsystem_impacts": {"suspension": 30},
        "explanation": "Vibrations that appear predominantly at highway cruising speeds (50-70 mph / 80-110 km/h) and disappear at lower city speeds are almost always caused by a rotating assembly imbalance: a missing wheel counterweight, bent wheel rim from a pothole, or uneven tire wear.",
        "risk_explanation": "While not an immediate safety hazard, chronic highway vibration accelerates wear on wheel bearings, tie-rod ends, ball joints, and causes premature scalloping (cupping) of tire treads.",
        "diy_checks": [
            "Check tire pressures on all four wheels when cold against the sticker on your driver's door jamb.",
            "Run your palm smoothly over the tire tread surface: feel for high and low wavy spots (cupping).",
            "Inspect wheel rims for packed dried mud or snow on the inside barrel, which acts as an unbalancing weight."
        ],
        "mechanic_questions": [
            "Can you perform a Road Force Balance on all four wheels?",
            "Are any wheel rims bent or tires showing tread separation or radial runout?",
            "Do wheel bearings or ball joints have any mechanical play?"
        ],
        "estimated_cost_tier": "Minor ($50 - $120 for 4-wheel road force balancing and tire rotation)"
    },
    {
        "id": "RULE_MOD_BATTERY_WEAK",
        "match_type": "any",
        "required_symptoms": ["slow_engine_crank", "clicking_when_starting"],
        "optional_symptoms": ["dim_flickering_lights"],
        "min_score": 65,
        "urgency": "moderate",
        "urgency_label": "MODERATE: Address Before Stranded",
        "title": "Depleted 12V Battery / Corroded Terminal Connections",
        "subsystem_impacts": {"electrical": 35},
        "explanation": "A slow sluggish crank or rapid clicking solenoid sound indicates that the starter motor is receiving insufficient electrical current (amperage). Most car batteries last 3 to 5 years before chemical plate degradation reduces Cold Cranking Amps (CCA).",
        "risk_explanation": "You risk getting completely stranded in a parking lot or cold morning when the battery voltage drops below the starter threshold.",
        "diy_checks": [
            "Check the date sticker on the top of the car battery: if it is over 3-4 years old, replacement is likely due.",
            "Inspect the positive (+) and negative (-) battery terminals for powdery white or bluish corrosion buildup.",
            "Ensure terminal cable clamps are tight—you should not be able to twist them by hand.",
            "Most auto parts stores (AutoZone, Advance Auto, O'Reilly) will test your battery and alternator for FREE in the parking lot."
        ],
        "mechanic_questions": [
            "What are the measured Cold Cranking Amps (CCA) versus the rated factory CCA?",
            "Can you clean and treat the battery cable clamps with anti-corrosion dielectric grease?",
            "Is there any parasitic battery drain drawing current while the car is parked and locked?"
        ],
        "estimated_cost_tier": "Minor ($120 - $220 for new quality battery with warranty)"
    },
    {
        "id": "RULE_MOD_WORN_BRAKE_PADS",
        "match_type": "all",
        "required_symptoms": ["brake_squealing"],
        "optional_symptoms": ["brake_warning_light"],
        "min_score": 58,
        "urgency": "moderate",
        "urgency_label": "MODERATE: Service Within 2-4 Weeks",
        "title": "Worn Brake Pad Wear Indicators (Acoustic Warning)",
        "subsystem_impacts": {"brakes": 35},
        "explanation": "Modern brake pads are engineered with small spring steel clips called 'wear indicators' (squealers). When the friction pad wears down to approximately 2-3mm, the metal finger touches the rotating disc to make a purposeful high-pitched squeal warning the driver before rotors are ruined.",
        "risk_explanation": "Ignoring this warning will wear down through the remaining friction material, progressing to metal-on-metal grinding which destroys the rotors and dramatically increases stopping distance.",
        "diy_checks": [
            "Inspect through wheel spokes: locate the brake caliper and look at the edge of the pad pressed against the rotor. New pads have ~10-12mm of thickness; under 3mm requires prompt replacement.",
            "Check if the squeal happens every time you apply the brakes, or only on the first cold stop in damp morning weather (surface rust).",
            "Check brake fluid reservoir under hood: fluid level naturally drops as pads wear thin."
        ],
        "mechanic_questions": [
            "What are the exact millimeter thickness measurements for the inner and outer brake pads?",
            "Can the rotors be cleaned and reused, or do they need to be replaced?",
            "Do the slide pins need to be cleaned and lubricated?"
        ],
        "estimated_cost_tier": "Minor to Moderate ($150 - $300 per axle)"
    },
    {
        "id": "RULE_MOD_POOR_FUEL_ECONOMY_MAF_O2",
        "match_type": "any",
        "required_symptoms": ["reduced_fuel_economy", "sluggish_acceleration"],
        "optional_symptoms": ["check_engine_light_steady", "engine_rough_idle", "black_exhaust_smoke"],
        "min_score": 62,
        "urgency": "moderate",
        "urgency_label": "MODERATE: Fuel Efficiency & Emissions Issue",
        "title": "Air-Fuel Sensor / Dirty MAF / Spark Plug Degradation",
        "subsystem_impacts": {"emissions_fuel": 35, "powertrain": 15},
        "explanation": "A sudden drop in MPG paired with sluggish acceleration typically means the engine control unit (ECU) cannot accurately meter fuel and air. A coated Mass Airflow (MAF) sensor wire, worn spark plug gaps, or a sluggish upstream Oxygen (O2) sensor causes the engine to run 'rich' (burning excess fuel).",
        "risk_explanation": "Wastes significant money on unnecessary fuel costs and eventually clogs the expensive catalytic converter with unburned hydrocarbons.",
        "diy_checks": [
            "Check your engine air filter: unclip the air box under the hood and look at the pleated paper filter. If packed with dirt, leaves, or bugs, replace it ($15 part).",
            "Verify all four tire pressures: underinflated tires by 5-10 PSI can decrease fuel economy by up to 5-10%.",
            "Check if you recently bought fuel from a low-grade unfamiliar station (bad fuel/ethanol mixture)."
        ],
        "mechanic_questions": [
            "What are the Short-Term and Long-Term Fuel Trim (STFT / LTFT) percentages on live scan tool data?",
            "Does the MAF sensor need cleaning with specialized electronic cleaner?",
            "Are the spark plugs past their recommended service interval (typically 60k-100k miles)?"
        ],
        "estimated_cost_tier": "Minor to Moderate ($25 for air filter DIY; $150 - $380 for spark plugs or O2 sensor)"
    },
    {
        "id": "RULE_MOD_SUSPENSION_CLUNK",
        "match_type": "any",
        "required_symptoms": ["clunking_over_bumps", "squeaking_over_bumps"],
        "optional_symptoms": ["steering_pulls_straight_road", "uneven_tire_wear"],
        "min_score": 58,
        "urgency": "moderate",
        "urgency_label": "MODERATE: Suspension Wear",
        "title": "Worn Sway Bar End Links, Strut Mounts, or Bushings",
        "subsystem_impacts": {"suspension": 35},
        "explanation": "Thumping or dull metallic clunking when negotiating driveway transitions, speed bumps, or potholes points to degraded suspension rubber bushings or loose ball-and-socket links, most commonly stabilizer bar (sway bar) end links or upper strut bearing plates.",
        "risk_explanation": "Decreases vehicle body roll stability during sharp cornering or emergency maneuvers. If ball joints or control arm bushings are severely worn, wheel alignment drifts and can eventually risk suspension component separation.",
        "diy_checks": [
            "With the car parked and key off, stand next to the front fender and vigorously push down on the car body to bounce it. Listen for creaking or bouncing more than 1.5 times.",
            "Inspect tires for feathering or uneven wear patterns across the contact patch.",
            "Look behind the front wheels with a flashlight: check for cracked, rotted rubber bushings or leaking hydraulic oil on the strut body."
        ],
        "mechanic_questions": [
            "Are the sway bar end links loose, or is the clunk originating from strut mounts or lower control arm ball joints?",
            "Will replacing this component require a four-wheel alignment afterward?",
            "Are the shocks/struts leaking hydraulic damping fluid?"
        ],
        "estimated_cost_tier": "Minor to Moderate ($120 - $250 for sway bar links; $400 - $800 for complete struts/control arms)"
    },
    {
        "id": "RULE_MOD_SOLID_CHECK_ENGINE",
        "match_type": "all",
        "required_symptoms": ["check_engine_light_steady"],
        "optional_symptoms": ["reduced_fuel_economy", "engine_rough_idle"],
        "min_score": 55,
        "urgency": "moderate",
        "urgency_label": "MODERATE: Read Diagnostic Trouble Codes",
        "title": "Stored OBD-II Diagnostic Trouble Code (DTC)",
        "subsystem_impacts": {"emissions_fuel": 40, "powertrain": 20},
        "explanation": "A steady (non-blinking) Check Engine Light indicates that the vehicle's On-Board Diagnostics computer has detected a sensor value outside factory parameters across multiple drive cycles. This can range from an EVAP fuel cap vapor leak to an O2 sensor or catalytic converter efficiency code.",
        "risk_explanation": "Safe to drive in the immediate term if the vehicle behaves normally and the light isn't blinking, but should be scanned soon to prevent compounding issues or failing emissions inspections.",
        "diy_checks": [
            "Ensure the fuel gas cap is screwed on tightly until it clicks 3 times. A loose cap is the #1 cause of code P0440 / P0455 (EVAP leak).",
            "Listen for unusual engine hiss or whistling (vacuum leak from a cracked rubber hose under the hood).",
            "Take the vehicle to any local auto parts retailer (they usually pull the OBD-II code for free)."
        ],
        "mechanic_questions": [
            "What specific alphanumeric DTC code was retrieved (e.g., P0420, P0171, P0442)?",
            "Was the freeze-frame data recorded at idle or cruising speed?",
            "Is this a single sensor fault, or is there an underlying mechanical cause?"
        ],
        "estimated_cost_tier": "Free DIY gas cap check; $50 - $350 for sensor replacement"
    },
    {
        "id": "RULE_ROUTINE_STEERING_PULL",
        "match_type": "all",
        "required_symptoms": ["steering_pulls_straight_road"],
        "optional_symptoms": ["uneven_tire_wear"],
        "min_score": 45,
        "urgency": "low",
        "urgency_label": "LOW: Routine Alignment / Tire Pressure",
        "title": "Wheel Alignment Drift or Unequal Tire Pressures",
        "subsystem_impacts": {"suspension": 35},
        "explanation": "If the vehicle drifts toward the road shoulder when traveling straight on flat highways without any braking input, the wheel camber/toe alignment has shifted out of specification (often from striking potholes or curbs) or one front tire has lower air pressure than the opposite side.",
        "risk_explanation": "Causes driver fatigue and rapid, expensive tire wear. Does not pose an imminent breakdown hazard.",
        "diy_checks": [
            "Check tire pressures on all 4 tires using a digital or pencil gauge. Even a 4-5 PSI difference between left and right front tires causes noticeable pull.",
            "Inspect tires for uneven tread wear or uneven shoulder scrub.",
            "Verify the pull happens on both left and right lanes of a multi-lane highway (to rule out normal road crown drainage slopes)."
        ],
        "mechanic_questions": [
            "Can you perform a computerized 4-wheel alignment check and provide a printout of before-and-after specs?",
            "Are the tie-rod adjustment sleeves seized with rust?"
        ],
        "estimated_cost_tier": "Minor ($80 - $140 for four-wheel laser alignment)"
    }
]

# Educational Pre-Mechanic Golden Checklist
GENERAL_DIY_CHECKLIST = [
    {
        "category": "Fluid Checks",
        "title": "Engine Motor Oil Level & Condition",
        "safety_tip": "Park on level ground. Wait 5-10 minutes after turning off engine.",
        "how_to": "Locate dipstick with yellow/orange handle. Pull out, wipe clean with rag, re-insert fully, pull out again. Oil should be between MIN/MAX holes. Golden amber is fresh; dark black is aged; milky tan indicates coolant contamination."
    },
    {
        "category": "Fluid Checks",
        "title": "Engine Coolant Expansion Reservoir",
        "safety_tip": "DANGER: NEVER loosen or open the radiator cap while the engine is warm or hot!",
        "how_to": "Look at the translucent plastic tank near the radiator. Check that the fluid level sits between the MIN and MAX embossed lines. Common colors are bright neon green, pink, or orange."
    },
    {
        "category": "Fluid Checks",
        "title": "Brake Fluid Reservoir",
        "safety_tip": "Brake fluid is corrosive to car paint. Do not spill.",
        "how_to": "Locate small clear reservoir near the driver's side firewall. Fluid should be light clear amber and near MAX line. If dark brown or near MIN, pads are worn or there is a leak."
    },
    {
        "category": "Visual Inspection",
        "title": "Under-Car Parking Spot Inspection",
        "safety_tip": "Place a clean piece of white cardboard under the engine bay overnight.",
        "how_to": "Check for drip colors: Brown/Black = Engine Oil; Neon Pink/Green = Coolant; Bright Red = Transmission or Power Steering; Clear/Water = Harmless A/C Condensation."
    },
    {
        "category": "Battery & Belts",
        "title": "12V Battery Terminals & Serpentine Belt",
        "safety_tip": "Do not touch both metal wrench and positive terminal to car metal simultaneously.",
        "how_to": "Inspect battery posts for fluffy white/blue crust. Check serpentine belt on the side of engine for fraying, cracks, or loose tension."
    }
]

# Mechanic Conversation Cheatsheet
MECHANIC_CONVERSATION_TIPS = [
    {
        "tip": "Describe Symptoms, Not Solutions",
        "detail": "Tell the mechanic WHAT you hear, feel, and smell ('I hear a metallic grinding when slowing down from 40 mph'), rather than instructing them what to replace ('Replace my rotors'). Let them confirm the diagnostic."
    },
    {
        "tip": "Ask for an Itemized Written Estimate",
        "detail": "Before authorizing repairs, request a breakdown separating parts cost from labor hours and diagnostic fees. Ask if OEM or quality aftermarket parts are used."
    },
    {
        "tip": "Request to See the Old Replaced Parts",
        "detail": "Legitimate shops are happy to show you your worn pads, burned belts, or fouled plugs. This verifies the work was actually performed."
    },
    {
        "tip": "Differentiate Urgent Safety from Recommended Maintenance",
        "detail": "If handed a long repair estimate, ask: 'Which of these items are critical safety issues today, and which can safely wait 3 to 6 months?'"
    }
]
