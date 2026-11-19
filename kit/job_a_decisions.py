"""
Job A: this job's decisions for the draft writer (write_draft.py).

Replaces draft_job_a.py (retired Nov 16, 2026). It holds only judgement for one job: which of
his lines apply, each quantity worked out in code from the job facts, where it came from, and
the reason. It writes no estimate file. The fixed rules of "03 Method" (marks, Ask default,
overlap groups, blank sub bids) are applied by write_draft.py, not here.

Holds none of his quantities, prices or costs. Row numbers are rows of his sheet.

Usage: python3 -I job_a_decisions.py job_a_decisions.json
Then:  python3 -I write_draft.py --lines his_lines.json --decisions job_a_decisions.json ...
"""
import json
import math
import sys

up = math.ceil

# ---- job facts (doc 08; source in brackets) ----
GAR_SF, GUEST_SF = 566, 576            # written, cover table
PERIM = 98                              # calculated from dims (22x27 less notch)
WALK_L, WALK_W = 17.5, 4 + 4/12         # dims A-2
WALK_SF = WALK_L * WALK_W               # 75.8
SUN_SF, PORCH_SF = 123, 12 * (14 + 4/12)
ROOF_SF = 828 + 50                      # calculated / scaled (doc 08 #16)
SIDING_SF = 1407                        # calculated (doc 08 #26)
BATH_SF = 54                            # written
WALL_H = 8                              # written, A-3 and A-4 (doc 08 #11). The old script used 9 ft on the upper level
GUEST_EXT, GUEST_INT = 96, 60           # dims 24x24; partitions from A-1 room dims (approx, doc 08 #37)
DOOR_WALL, DOOR_W = 22, 18              # dims
EAVE = 2 * (24 + 2 * 16/12)             # two eaves incl. 1'4" overhangs
RAFTER_LEN = (12 + 16/12) * math.hypot(12, 5) / 12   # 5:12
RAKE = 4 * RAFTER_LEN
TRIM_RUN = EAVE + RAKE

D = {}
IN, ASK, OUT = "in", "ask", "out"


def put(row, scope, qty, src, conf, why, pm=False, kind=None, flags=None, cross=False, page=None):
    """One decision. pm = plan minimum (bare plan count, no waste guessed for him)."""
    d = {"scope": scope, "reason": why, "confidence": conf}
    if qty is not None:
        d["qty"] = qty
        d["source"] = {"type": src, "page": page, "rule": why if src in ("calculated", "assumed") else None}
    if pm:
        d["plan_minimum"] = True
    if kind:
        d["kind"] = kind
    if flags:
        d["flags"] = flags
    if cross:
        d["cross_checked"] = True
    D[row] = d


# Division 1
put(6, IN, 1, "assumed", "medium", "New building needs a permit; lump sum")
put(7, ASK, None, "", "low", "His call whether an expeditor is used")
put(8, IN, 1, "assumed", "medium", "Standard on a new structure")
put(9, ASK, None, "", "low", "Site plan already exists; who paid for the survey is his to say")
put(10, ASK, None, "", "low", "New footprint near setbacks; his call")
put(11, ASK, None, "", "low", "Not on plans")
put(12, ASK, None, "", "low", "Occupied house next to the work; his call")
put(13, IN, None, "", "low", "Applies; months depend on his schedule")
put(14, IN, 1, "assumed", "medium", "Standard")
put(15, ASK, None, "", "low", "Engineered header detail is already on A-6; was the engineer his cost?")
put(16, ASK, None, "", "low", "New sewer line and driveway work may touch the street")
put(17, IN, None, "", "low", "Applies (garage demo, new build); count is his")
put(18, IN, 1, "assumed", "medium", "Standard")
put(19, IN, 1, "assumed", "medium", "Standard")
put(20, ASK, None, "", "low", "Unit is each; his rule not known")
put(21, IN, 1, "assumed", "medium", "Standard")
put(23, IN, 1, "written", "medium", "Site plan carries erosion and stormwater notes")
# Division 2
put(29, IN, 1, "written", "high", "Plans: remove garage (299 sf), stone paving, patio fireplace, two steps")
put(30, ASK, None, "", "low", "Plans show 438 sf of stone paving removed; no concrete drive demo written")
put(31, ASK, None, "", "low", "Old garage; hidden condition", flags=["hidden_condition"])
put(33, IN, 1, "written", "medium", "Site plan: cut about 8 CY, fill about 12 CY")
put(34, IN, 1, "written", "medium", "Site plan says spoil is hauled off")
put(35, IN, 1, "assumed", "medium", "Follows the grading")
put(36, IN, 1, "assumed", "low", "12 CY of fill written = about one load")
put(37, ASK, None, "", "low", "Arborist sheets exist but were not re-read this run")
put(40, ASK, None, "", "low", "Not on plans")
put(41, IN, 1, "written", "medium", "Stormwater notes on the site plan")
put(43, IN, 1, "written", "medium", "Plans: move existing 6 ft fence")
put(44, IN, None, "", "low", "New 6 ft fence shown; length not dimensioned on the plans")
# Division 3
put(49, IN, None, "", "low", "Applies; hours are his")
put(50, IN, 1, "assumed", "low", "About 10 CY of demo debris written = one load")
put(52, ASK, None, "", "low", "Slab with turn-down, no foundation walls drawn; 3 stair post footings")
put(53, ASK, None, "", "low", "Access to rear of lot; his call")
put(57, IN, 2, "assumed", "medium", "His line is worded as two days")
put(58, IN, round(GAR_SF + WALK_SF), "calculated", "medium", "Garage slab 566 + walkway slab 76")
put(59, IN, None, "", "low", "No grade beam drawn; he may add one at the door. His build rule not recorded")
put(60, IN, None, "", "low", "Applies; count is his method")
put(61, IN, 1, "assumed", "medium", "Slab over 500 sf")
put(62, IN, None, "", "low", "Anchor spacing not read this run")
put(63, ASK, None, "", "low", "Stair lands on grade; pad not drawn")
put(64, IN, 3, "counted", "medium", "3 stair post footings written as 16x16x12; his line says 2x2",
    flags=["plans_vs_estimate"])
put(66, IN, 1, "assumed", "medium", "Follows the footing")
put(67, IN, 1, "assumed", "low", "8 CY of cut written = one load")
put(69, IN, up(PERIM * 2), "calculated", "medium", "(2) #4 continuous x 98 LF, no lap added; he may add more", pm=True)
slab_cy = GAR_SF * (4/12) / 27 + PERIM * 1.0 * (8/12) / 27
put(70, IN, round(slab_cy, 1), "calculated", "low",
    "Drawn minimum only (4 in. slab + 12 in. turn-down), no waste added. He builds footings bigger than drawn; his rule is not recorded", pm=True)
walk_cy = WALK_SF * (4/12) / 27 + (WALK_L + 2 * WALK_W) * 1.0 * (8/12) / 27
put(71, IN, round(walk_cy, 1), "calculated", "low", "Drawn minimum, no waste added; same caution as the slab", pm=True)
put(72, IN, None, "", "low", "6x6 mesh over 642 sf; his unit is not stated")
put(73, IN, 1, "assumed", "low", "4 in. gravel under 642 sf = 8 CY = one load")
put(74, IN, 1, "assumed", "medium", "Vapor barrier under slab")
put(75, ASK, None, "", "low", "Same question as the pump above")
put(76, IN, 1, "assumed", "medium", "Slab edge forms")
put(79, IN, 1, "written", "high", "544 sf permeable pavers over 8 in. stone, written")
put(81, ASK, None, "", "low", "Driveway extension is drawn as permeable pavers; is any concrete drive his?")
put(82, ASK, None, "", "low", "Not drawn")
put(85, ASK, None, "", "low", "Not drawn")
put(86, ASK, None, "", "low", "Two 6 in. steps down at the screen porch; material not stated")
# Division 4
put(111, ASK, None, "", "low", "Patio fireplace removed; patio repair area not on plans")
# Division 5
put(118, IN, None, "", "low", "A325 bolts at the garage header; count is on A-6, not re-read")
put(119, IN, 1, "written", "medium", "Steel flitch plates at the garage door header (engineer's detail)", flags=["engineering"])
put(120, ASK, None, "", "low", "Stair guard is drawn as wood; gripable handrail material not stated")
# Division 6 framing labor (133, 134, 137 sit in an overlap group with his lump-sum row 125: see OVERLAPS)
put(125, ASK, None, "", "low", "His framing labor lump-sum row")
put(133, ASK, GAR_SF, "written", "high", "Area table")
put(134, ASK, GUEST_SF, "written", "high", "Area table")
put(137, ASK, round(SUN_SF + PORCH_SF + WALK_SF), "calculated", "medium", "Sunroom 123 + porch 172 + walkway 76; what he counts here is not known")
put(138, IN, 1, "counted", "medium", "One exterior stair, 15 risers")
put(139, IN, 1, "assumed", "medium", "His sheet carries Zip sheathing")
put(135, ASK, None, "", "low", "His practice")
# Garage walls (rows 148 and 149 are read as headings on his line list: see HEADING_ROWS)
put(150, IN, 2, "calculated", "low", "One 2'8\" door header", pm=True)
put(151, IN, 3 * (DOOR_W + 2), "calculated", "low",
    "ENGINEERING: plans say (3) 1-3/4 x 11-7/8 LVL, his line says 14 in. 3 plies x 20 ft", pm=True, flags=["engineering"])
gar_24 = PERIM - DOOR_WALL
put(152, IN, gar_24, "calculated", "low", "One stud per foot of 2x4 wall (76 LF). Plans and supplier list disagree on 2x6 walls", pm=True)
put(153, IN, up(gar_24 / 16), "calculated", "medium", "Treated bottom plate, 76 LF", pm=True)
put(154, IN, up(gar_24 * 2 / 16), "calculated", "medium", "Double top plate, 76 LF", pm=True)
put(155, IN, up(PERIM * WALL_H / 32), "calculated", "medium", "98 LF x 8 ft walls, no waste added", pm=True)
put(156, IN, None, "", "low", "Not read this run")
# Guest house level (rows 160 and 165 are read as headings on his line list: see HEADING_ROWS)
put(159, IN, 1, "written", "medium", "Supplier list: 16 in. joists, 24 ft. Supplier pages are another job's title block")
put(161, IN, up(GUEST_SF / 32), "calculated", "medium", "576 sf subfloor, no waste added", pm=True)
put(162, IN, up((GUEST_EXT + GUEST_INT) * 3 / 16), "calculated", "low", "3 plates x (96 exterior + about 60 interior LF)", pm=True)
put(163, IN, GUEST_EXT + GUEST_INT, "calculated", "low", "One stud per foot of wall; partitions added from room dims", pm=True)
put(164, IN, 12, "calculated", "low", "6 openings x 2", pm=True)
put(166, IN, None, "", "low", "Ceiling framing not read this run")
put(167, IN, 2 * (up(24 / (16/12)) + 1) + 4, "calculated", "medium",
    "2x8 rafters @16 in. over 24 ft, both sides, + 4 at the rakes. Length needed 14.4 ft", pm=True)
put(168, IN, None, "", "low", "Cross gable over the stair not measured")
put(169, IN, up(2 * (24 + 2 * 16/12)), "calculated", "low", "(2) 2x12 ridge x 26.7 ft", pm=True)
put(170, IN, 1, "assumed", "medium", "Lump sum")
put(171, ASK, None, "", "low", "Use on this level not clear")
put(172, IN, up(ROOF_SF / 32), "calculated", "medium", "878 sf sloped, no waste added", pm=True)
put(173, IN, None, "", "low", "Rolls per sheet is his rule")
# Walkway
put(176, IN, 2, "counted", "medium", "Two 6x6 posts drawn at the breezeway")
put(177, IN, 2, "counted", "medium", "One per post")
put(178, IN, 4, "calculated", "low", "Beam 17.5 ft, 2 plies. Plans say (2) 2x12, his line says 2x10", pm=True, flags=["plans_vs_estimate"])
put(179, IN, up(WALK_L / (16/12)) + 1, "calculated", "low", "Rafters @16 in. over 17.5 ft (spacing assumed)", pm=True)
put(180, IN, 1, "assumed", "medium", "Lump sum")
put(181, IN, up(WALK_L * (WALK_W + 1.5) / 32), "calculated", "low", "Roof 17.5 x 5.8 ft, no waste added", pm=True)
put(182, IN, 2, "counted", "medium", "One per post")
# Stairs
put(185, IN, 3, "counted", "medium", "3 stair posts on footings. Landing is 9.4 ft up: 8 ft posts look short")
put(186, IN, None, "", "low", "Landing framing not detailed")
put(187, IN, 5, "calculated", "low", "Guard posts about every 6 ft over 26 ft", pm=True)
put(188, IN, 3, "calculated", "medium", "3 stringers, 15 ft each (14 treads @10 in., 9.4 ft rise)", pm=True)
put(189, IN, None, "", "low", "Not detailed")
put(190, IN, 1, "assumed", "medium", "Lump sum")
put(191, IN, up(26 * 12 / 4.5 / 4), "calculated", "low", "Pickets @4.5 in. over 26 ft of guard, 4 per 12 ft piece", pm=True)
put(192, IN, up((14 * 2 * 3 + 36) / 16), "calculated", "low", "14 treads x 2 boards x 3 ft + landing (about 36 LF of decking, assumed)", pm=True)
put(193, IN, 1, "assumed", "medium", "Lump sum")
# Porch / sunroom framing
put(195, IN, None, "", "low", "One 6x6 post labelled on A-1; others not confirmed")
put(196, IN, None, "", "low", "Sunroom walls sit on the existing patio; not taken off this run")
put(197, IN, None, "", "low", "As above")
put(198, IN, None, "", "low", "Follows post count")
put(199, IN, None, "", "low", "Follows post count")
put(200, IN, None, "", "low", "Roof shape over sunroom and porch not read this run")
put(201, IN, up((12 + 8 + 8/12) / (16/12)) + 1, "calculated", "low",
    "PLANS VS HIS LINE: plans say 2x6 rafters, his line says 2x8x14. Count @16 in. over 20.7 ft", pm=True, flags=["plans_vs_estimate"])
put(202, IN, up((12 + 8 + 8/12 + 1) * (14.33 + 1.33) / 32), "calculated", "low", "Roof about 21.7 x 15.7 ft at 3:12, no waste added", pm=True)
put(203, IN, None, "", "low", "Sunroom window headers not taken off")
put(204, IN, None, "", "medium", "His tax line (percent)")
put(205, IN, None, "", "medium", "His contingency line (percent)")
# Interior trim
put(209, IN, 1, "assumed", "medium", "Guest house and sunroom")
put(213, IN, 14, "counted", "low", "5 guest house openings + 9 sunroom windows; he may count units")
put(214, IN, up((GUEST_EXT + 2 * GUEST_INT - 25 + 46) / 16), "calculated", "low", "Wall base: 96 exterior + 2 sides of 60 interior, less about 25 LF of door openings, plus about 46 LF at the sunroom (assumed) = about 237 LF; 16 ft pieces assumed", pm=True)
put(221, IN, 1, "assumed", "medium", "Lump sum")
put(222, ASK, None, "", "low", "Use not known")
# Division 7
put(243, IN, 1, "written", "high", "R-13 walls, R-38 ceiling, R-19 floor written")
put(251, IN, 1, "written", "low", "Sub bid. Roof 8.8 squares + low-slope roofs. CONFLICT on 3:12 roofs: shingles (A-5) vs rolled roofing (A-3)", kind="sub_bid")
put(254, IN, 2, "written", "high", "Two 44x46 tempered skylights written on A-1", page="A-1")
put(258, IN, 1, "assumed", "medium", "Fascia and soffit drawn")
put(259, IN, 1, "written", "medium", "Band board written")
put(260, ASK, None, "", "low", "Lump sum or by the square? His call")
put(261, IN, 1, "written", "medium", "Brackets written; count not read this run")
put(262, IN, 1, "written", "medium", "Covered breezeway")
put(263, IN, 1, "written", "medium", "Sunroom")
put(264, ASK, 1, "counted", "medium", "17 window units, 3 doors")
put(265, ASK, round(SIDING_SF / 100, 1), "calculated", "medium", "1,407 sf net siding")
put(266, IN, round(TRIM_RUN), "calculated", "medium", "Eaves 53 + rakes 58 LF, garage roof only")
put(267, IN, PERIM, "calculated", "medium", "Band at the floor line, 98 LF")
put(268, IN, 1, "assumed", "low", "Garage walls 784 sf (upper walls are Zip)")
put(270, IN, None, "", "low", "Brackets written; count is on the elevations, not re-read")
put(271, ASK, None, "", "low", "Overlaps the install lump sum above")
put(272, IN, 3, "counted", "high", "3 exterior doors")
put(273, ASK, None, "", "low", "His unit not clear")
put(277, IN, up(SIDING_SF / 7), "calculated", "medium",
    "1,407 sf / 7 sf per piece, no waste added", pm=True)
open_lf = 14.3 + 2 * 21 + 10.3 + 21 + 16.3 + 16 + 32
put(278, ASK, up(open_lf / 12), "calculated", "low", "Trim around 6 window openings, 2 doors, garage door: 152 LF, no waste added", pm=True)
put(279, ASK, 16, "calculated", "low", "4 full-height corners x 3 pieces + 2 notch corners x 2", pm=True)
put(280, IN, up(TRIM_RUN / 12), "calculated", "medium", "111 LF, no waste added", pm=True)
put(281, IN, up(TRIM_RUN / 12), "calculated", "low", "111 LF, no waste added; 12 ft pieces assumed", pm=True)
put(282, IN, None, "", "low", "Where he uses it is not known")
put(283, IN, up(TRIM_RUN / 12), "calculated", "low", "Frieze at eaves and rakes, 111 LF, no waste added", pm=True)
put(284, IN, up(TRIM_RUN / 10), "calculated", "low", "111 LF, no waste added; 10 ft pieces assumed", pm=True)
put(285, IN, up(PERIM / 12), "calculated", "medium", "98 LF, no waste added", pm=True)
for r in (288, 289, 290, 291, 292, 293, 294, 296):
    put(r, IN, None, "", "low", "Sunroom and porch trim: needs the elevations, not re-read this run")
put(295, IN, 1, "assumed", "medium", "Roof-to-wall flashing at the house")
put(297, IN, None, "", "medium", "His tax line (percent)")
put(298, IN, None, "", "medium", "His contingency line (percent)")
put(300, ASK, None, "", "low", "Overlaps the piece counts above")
put(302, IN, 1, "assumed", "medium", "Lump sum")
put(303, IN, 1, "assumed", "medium", "Lump sum")
put(313, IN, 1, "written", "medium", "Screen panels drawn")
put(314, IN, 1, "counted", "high", "One 3068 screen door")
put(315, IN, 1, "assumed", "medium", "Lump sum")
put(319, ASK, None, "", "low", "Porch ceiling finish not on plans (172 sf if used)")
for r in (320, 321, 322, 323, 325):
    put(r, ASK, None, "", "low", "Porch trim finish not on plans")
put(345, IN, 1, "written", "medium", "Plans say 5 in. ogee gutters; ogee is the common name for the K profile")
# Division 8
put(350, IN, 4, "counted", "high", "Laundry, bath, bedroom, coats", page="A-1")
put(351, IN, 1, "counted", "high", "One 4'8\" pair at the closet", page="A-1")
put(358, ASK, None, "", "low", "Attic access not drawn")
put(361, IN, 5, "counted", "medium", "4 singles + 1 pair")
put(364, IN, 3, "counted", "high", "3 exterior doors")
put(368, IN, 1, "counted", "high", "Guest house entry")
put(369, IN, 1, "counted", "medium", "PLANS VS HIS LINE: garage door drawn 2'8\" wide, his line says 2'6\"", flags=["plans_vs_estimate"])
put(370, IN, 1, "counted", "medium", "PLANS VS HIS LINE: sunroom door drawn 2'8\" x 7'0\", his line says 2'6\"", flags=["plans_vs_estimate"])
put(381, IN, 5, "counted", "high", "Sunroom, cross-checked on A-1", cross=True, page="A-1")
put(382, IN, 4, "counted", "high", "Sunroom tempered, cross-checked", cross=True, page="A-1")
put(383, IN, 2, "counted", "high", "Two pairs, great room; cross-checked with the elevations (doc 08)", cross=True)
put(384, IN, 1, "counted", "high", "One pair, wet bar wall; cross-checked with the elevations (doc 08)", cross=True)
put(385, IN, 1, "counted", "high", "Bath, tempered; cross-checked with the elevations (doc 08)", cross=True)
put(386, IN, 1, "counted", "high", "One egress pair, bedroom; cross-checked with the elevations (doc 08)", cross=True)
put(389, ASK, None, "", "low", "Overlaps the install lump sum in Division 7")
put(390, IN, 1, "assumed", "medium", "Lump sum")
put(393, IN, 1, "written", "high", "One 18x7 overhead door")
put(394, IN, 1, "assumed", "medium", "Not on plans; standard with the door")
# Division 9
put(399, IN, 1, "written", "low", "Sub bid. Includes 5/8 Type X garage ceiling (566 sf)", kind="sub_bid")
put(403, ASK, None, "", "low", "His practice")
put(409, ASK, 60, "calculated", "low", "Tub surround 10 LF x 6 ft")
put(410, ASK, BATH_SF, "written", "medium", "Bath 5'0\" x 10'9\"")
put(415, ASK, None, "", "low", "Laundry floor finish not on plans (43 sf)")
put(417, ASK, None, "", "low", "Wet bar backsplash not on plans")
put(422, IN, 4, "calculated", "low", "60 sf of surround / 15 sf sheets")
put(426, IN, None, "", "low", "Bags per sf is his rule")
put(427, IN, None, "", "low", "Bags per sf is his rule")
put(437, ASK, GUEST_SF - BATH_SF, "calculated", "low", "Client choice: floor finish not on plans. 522 sf if LVT throughout except the bath", kind="client_choice")
put(439, ASK, None, "", "low", "Client choice: floor finish not on plans", kind="client_choice")
put(441, IN, 1, "assumed", "low", "Sub price; size-dependent lump sum")
put(442, IN, 1, "assumed", "low", "Porch and breezeway")
# Division 10
put(448, IN, None, "", "low", "One bath; his unit is days")
put(449, ASK, None, "", "low", "Tub/shower drawn; door or curtain is a client choice", kind="client_choice")
put(451, IN, 1, "assumed", "medium", "One bath")
# Division 12 (464 and 481 sit in overlap groups: see OVERLAPS)
put(463, IN, 1, "counted", "medium", "One vanity. Three linen cabinets also drawn")
put(464, ASK, 1, "counted", "low", "Wet bar, L-shaped; cabinet list is a selection")
put(471, IN, None, "", "low", "Days are his")
put(481, ASK, 27, "calculated", "low", "Wet bar top scaled at about 13 LF x 25 in.")
put(482, IN, 2, "counted", "medium", "Bar sink and vanity sink")
put(483, ASK, None, "", "low", "Vanity top about 6 sf")
# Division 14
put(491, ASK, None, "", "low", "New dwelling unit; code test likely")
put(492, IN, 1, "assumed", "low", "Sub bid. No mechanical plan; one system for 576 sf", kind="sub_bid")
put(495, IN, 1, "counted", "medium", "Washer/dryer drawn")
put(498, ASK, None, "", "low", "Fuel not on plans")
put(500, IN, 1, "counted", "medium", "One bath")
# Division 15 (507, 509 and the fixture list sit in an overlap group: see OVERLAPS)
put(506, IN, 1, "assumed", "medium", "Standard")
put(507, ASK, 1, "counted", "low", "Sub bid. Fixtures drawn: tub/shower, toilet, lav, bar sink, washer, utility sink, hose bibb", kind="sub_bid")
put(509, ASK, None, "", "low", "No plumbing sheet in the set. What he counts on this line is not recorded")
put(510, ASK, None, "", "low", "30 in. refrigerator drawn; icemaker not stated")
put(514, IN, 1, "counted", "medium", "Laundry is on the upper floor")
put(515, IN, 1, "counted", "high", "One spigot drawn at the garage")
for r, q, w in ((522, 1, "One lav"), (523, 1, "One toilet"), (524, 1, "One tub/shower"), (528, 1, "One spigot"),
                (529, 1, "Bar sink"), (533, 1, "Washer drawn"), (534, 1, "Garage utility sink"), (537, 1, "Upper-floor laundry")):
    put(r, ASK, q, "counted", "medium", w)
put(531, ASK, None, "", "low", "No water heater drawn; one is needed")
put(538, ASK, None, "", "low", "Not stated")
put(540, IN, 1, "written", "low", "New 6 in. sanitary line with clean-out written; length not dimensioned")
for r, w in ((542, "Lav faucet"), (543, "Tub/shower set"), (545, "Lav sink"), (546, "Bathtub"), (554, "Bar faucet"),
             (555, "Bar sink"), (559, "Toilet")):
    put(r, IN, 1, "counted", "medium", w + "; client choice", kind="client_choice")
put(556, IN, 1, "counted", "medium", "Garage utility sink")
put(561, ASK, None, "", "low", "No water heater drawn; size is his call")
# Division 16 (569, 570 and 576 sit in an overlap group: see OVERLAPS. Row 571 is read as a heading: see HEADING_ROWS)
put(567, ASK, None, "", "low", "His call")
put(568, IN, 1, "assumed", "medium", "Standard; his unit reads SF")
put(569, ASK, None, "", "low", "No electrical sheet in the set")
put(570, ASK, GUEST_SF, "written", "low", "Sub bid by the square foot; no electrical plan", kind="sub_bid")
put(572, IN, None, "", "low", "No electrical plan")
put(574, ASK, None, "", "low", "Not on plans")
put(576, ASK, None, "", "low", "No electrical sheet in the set")
put(577, ASK, None, "", "low", "Existing service size unknown")
put(578, IN, 1, "assumed", "low", "Allowance", kind="allowance")
put(579, ASK, None, "", "low", "Not on plans")
# Appliances
for r in (584, 590, 594):
    put(r, ASK, None, "", "low", "30 in. refrigerator and washer/dryer drawn; who supplies is a client choice", kind="client_choice")
put(599, IN, None, "", "medium", "His overhead and profit line (percent)")

# His lines for the same work: one question each (Method step 4). No usual line is named: the only
# recorded notes come from this same job, and a one-job note is never used on the job it came from.
OVERLAPS = [
    {"rows": [125, 133, 134, 137], "confirmed": False,
     "question": "Framing labor: one lump sum, or by the square foot per level?"},
    {"rows": [569, 570, 576], "confirmed": False,
     "question": "Electrical: the main bid, the apartment bid by the square foot, or the detached garage lump sum?"},
    {"rows": [507, 509, 522, 523, 524, 528, 529, 533, 534, 537], "confirmed": False,
     "question": "Plumbing: one bid, install by a count, or the per-fixture list?"},
    {"rows": [464, 465, 466, 467, 468], "confirmed": False,
     "question": "Wet bar cabinets: the kitchen cabinet lump sum, or the cabinet sub-lines?"},
    {"rows": [481, 478], "confirmed": False,
     "question": "Wet bar top: which counter line?"},
    {"rows": [260, 265], "confirmed": False, "question": "Siding labor: lump sum, or by the square?"},
    {"rows": [264, 271, 389], "confirmed": False, "question": "Setting windows and doors: which of these lines?"},
    {"rows": [300, 278, 279], "confirmed": False, "question": "Corner boards and window trim: by the piece list, or on the one line?"},
    {"rows": [53, 75], "confirmed": False, "question": "Concrete pump: which line, if one is needed?"},
    {"rows": [402, 406, 409, 411, 414], "confirmed": False, "question": "Guest house bath wall tile: which of your bath lines?"},
    {"rows": [404, 407, 410, 412, 413], "confirmed": False, "question": "Guest house bath floor tile: which of your bath lines?"},
    {"rows": [483, 484, 485], "confirmed": False, "question": "Vanity top: which counter line?"},
]

# His rows that the line list reads as headings, because he left them empty on the job the list was made
# from. The writer cannot carry a decision on a heading, so what the plans say is shown on the cover.
HEADING_ROWS = [
    f"His row 148 (2x6x16PT) is read as a heading. Plan minimum: {up((DOOR_WALL - DOOR_W) / 16)} piece, bottom plate at the 2x6 door wall.",
    f"His row 149 (2x6x10) is read as a heading. Plan minimum: {DOOR_WALL - DOOR_W + 6} studs at the door wall. Plans and supplier list disagree (supplier list: 98).",
    f"His row 165 (Zip wall) is read as a heading. Plan minimum: {up((GUEST_EXT * WALL_H + 120) / 32)} sheets (96 LF x 8 ft + gables 120 sf).",
    "His row 160 (2x6x16PT, upper level) is read as a heading. Use on this level is not clear from the plans.",
    "His row 571 (power for garage area) is read as a heading. No electrical sheet in the set.",
]

# Rows whose answer was already visible in docs 07/08 before the first draft (Nov 16). For scoring only.
SEEN = [8, 44, 58, 59, 70, 176, 185, 201, 254, 277, 345, 350, 351, 361, 368, 369, 370,
        381, 382, 383, 384, 385, 386, 410, 437, 540]

DECISIONS = {
    "job": {"id": "jobA-draft-2026-11-16-remake", "job": "Job A", "job_type": "mixed", "parts": ["adu", "renovation"],
            "definition_level": "permit_plans",
            "note": "Draft estimate. Not a bid. Scope and quantities only: no prices. Remake of the Nov 16 blind draft through the draft writer."},
    "cover": {
        "missing_pages": [
            "No electrical, plumbing or mechanical sheets in the set.",
            "Elevations, sections and roof framing were not re-read for this draft; lines that need them are blank.",
            "Arborist sheets not re-read.",
            "Lumber supplier pages are 2 of 4, carry another job's title block and are marked not released.",
        ],
        "assumptions": [
            "No written scope list for the renovation part. The sunroom and porch are drafted from the plans as new construction on the existing patio.",
            "Lumber, sheathing, trim, concrete and rebar are plan minimum: the bare plan count, with no waste or overage added.",
            "Lines with no rule yet are Ask, not Out.",
        ] + HEADING_ROWS,
        "exclusions": [],
        "range": None,
    },
    "lines": {str(r): d for r, d in sorted(D.items())},
    "overlaps": OVERLAPS,
    "new_lines": [
        {"description": "Washer and dryer", "division": 17, "why": "Drawn in the laundry; no line on his sheet outside the appliance suite"},
        {"description": "Linen cabinets (3)", "division": 12, "why": "Drawn in laundry and bath"},
        {"description": "Closet shelves and rod", "division": 6, "why": "Written in the laundry"},
        {"description": "Smoke and CO detectors", "division": 16, "why": "Drawn; probably inside his electrical bid"},
        {"description": "Cat door", "division": 8, "why": "Drawn at the screen porch"},
    ],
    "seen_before": SEEN,
}

if __name__ == "__main__":
    with open(sys.argv[1], "w") as f:
        json.dump(DECISIONS, f, indent=1)
    print("decisions written:", len(D), "lines,", len(OVERLAPS), "overlap groups,", len(DECISIONS["new_lines"]), "new lines")


# Change log
# Nov 16, 2026 · New file. Job A's decisions moved here from draft_job_a.py, which is retired. Changes made
#   in the move (all from the Nov 16 review and the approved Method changes):
#   - Guessed waste removed from 16 quantity rules; lumber, sheathing, trim, concrete and rebar are plan minimum.
#   - Upper-level wall height is the written 8 ft, not 9 ft (it fed the Zip wall row, now a cover note).
#   - 12 overlap groups, each one question; their lines are Ask until he confirms his usual line.
#   - Sub bids, client choices and the one allowance carry their kind, so their price stays blank.
#   - Flags added for plans-versus-his-line, engineering and hidden conditions.
#   - "Cross-checked" kept only for the window counts; door counts are counted once.
#   - Five of his rows are headings on the line list and cannot take a decision; they are cover notes.
#   - Reasons no longer mention his figures. Rows with no decision are left to the writer (Ask).
# Nov 16, 2026 (after the fresh review) · Five "one load / one roll" quantities (rows 36, 50, 67, 73, 268) are now
#   assumed, so Low. No usual line is named in the overlap questions and the siding reason no longer quotes
#   the 1.07 ratio: both were his answers for this same job. Two constants explained (rows 192, 214).
