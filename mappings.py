AUTHOR_MAP = {
    'Tonya Dewey': 'Tonya Kim Dewey-Findell',
    'Tijmen Pronk': 'Tijman Pronk',
    'Ganesh Gupta': '',
    'Henrik Liljegren': '',
    'Simone Loi': '',
    'Ulrich Geupel': '',
    'Shervin Farridnejad': '',
    'Adam Benkato': '',
    'Mandar Purandare': '',
    'Sam Mersch': '',
    'Borana Lushaj': '',
    'Asfar Ali Khan': '',
    'Patrycja Markus': '',
    'Nicholas Sims-Williams': '',
    'Paul Videsott': '',
    'Paul Versloot': '',
    'Charalambos Christodoulou': '',
    'Guto Rhys': '',
    'Annemarie Verkerk': '',
    'Mojtaba Gheitasi': '',
    'Harald Hammarstr\xf6m': '',
    'Giorgio Cadorini': '',
    'Lo\xefc Cheveau': '',
    'Arash Zeini': '',
    'J\xe9r\xe9mie Delorme': '',
    'Lars Steensland': '',
    'Manuel Widmer': '',
    'Stephen Dworkin': '',
    'Esther Baiwir': '',
    'Khawaja Rehman': '',
    'Sabine Tittel': '',
    'Heather Pagan': '',
}

"""
clade
    id
    cladeName
    hexColor
    shortName
    export
    exportDate
    taxonsetName
    atMost
    atLeast
    distribution
    uniformUpper  # always empty
    uniformLower  # always empty
    cladeLevel0
    cladeLevel1
    cladeLevel2
    cladeLevel3
    level0Name
    level1Name
    level2Name
    level3Name
languagelist
    id
    name
    description
languageclade
    id
    cladesOrder
    clade_id
    language_id
romanisedsymbol
    id
    symbol
sndcomp
    id
    lgSetName
    lv0
    lv1
    lv2
    lv3
    cladeLevel0
    cladeLevel1
    cladeLevel2
    cladeLevel3
meaninglist
    id
    name
    description
languagelistorder
    id
    language_id
    language_list_id
    order
"""

FIELD_MAP = {
    'author':
        {
            "id": "ID",
            "surname": "Last_Name",
            "firstNames": "First_Name",
            "email": "",
            "website": "URL",
            "initials": "",
            "user_id": "",
        },
    'lexeme':  # -> forms.csv
        {
            "id": "ID",
            "language_id": "Language_ID",
            "meaning_id": "Parameter_ID",
            "romanised": "Form",
            "phon_form": "phon_form",
            "gloss": "Gloss",
            "notes": "Comment",
            "_order": "",
            "dubious": "",
            "not_swadesh_term": "",
            "phoneMic": "Phonemic",
            "rfcWebLookup1": "url",
            "rfcWebLookup2": "",  # all empty
            "nativeScript": "native_script",
        },
    'language':  # -> languages.csv
        {
            "id": "ID",  # -> id
            "iso_code": "Iso",  # -> iso639P3code
            "ascii_name": "ascii_name",
            "utf8_name": "Name",  # -> Name
            "description": "Description",
            "earliestTimeDepthBound": "Earliest_Time_Depth_Bound",
            "latestTimeDepthBound": "Latest_Time_Depth_Bound",
            "progress": "",
            "author": "Authors",
            "foss_stat": "fossil",
            "glottocode": "Glottocode",  # -> glottocode
            "level0": "",
            "level1": "",
            "level2": "",
            "level3": "",
            "low_stat": "",  # always False
            "representative": "",
            "reviewer": "",
            "rfcWebPath1": "url",
            "rfcWebPath2": "",  # all empty
            "soundcompcode": "",
            "variety": "Variety",
            "sortRankInClade": "",
            "sndCompLevel0": "",
            "sndCompLevel1": "",
            "sndCompLevel2": "",
            "sndCompLevel3": "",
            "entryTimeframe": "",
            "originalAsciiName": "",
            "historical": "historical",
            "notInExport": "notInExport",
            "distribution": "",
            "uniformLower": "",
            "uniformUpper": "",
            "latitude": "Latitude",  # -> Latitude
            "longitude": "Longitude",  # -> Longitude
            "exampleLanguage": "",
            "fragmentary": "",
        },
    'meaning':  # -> parameters.csv
        {
            "id": "ID",
            "gloss": "Name",
            "description": "",  # always empty!
            "notes": "",  # always empty!
            "percent_coded": "",
            "doubleCheck": "",
            "exclude": "",
            "meaningSetIx": "",
            "tooltip": "Description",
            "meaningSetMember": "",
            "exampleContext": "Example_Context",
            "ixElicitation": "",
            "concepticon_id": "Concepticon_ID",
        },
    'cognatejudgement':  # -> cognates.csv
        {
            "id": "ID",
            "lexeme_id": "Form_ID",
            "cognate_class_id": "Cognateset_ID",
        },
    'cognateclass':
        {
            "id": "ID",
            "root_form": "Root_Form",
            "gloss_in_root_lang": "Root_Gloss",
            "root_language": "Root_Language",
            # alias
            "notes": "Comment",
            # name  - always empty

            "loan_notes": "loan_notes",
            "loan_source": "loan_source",  # pretty variable languoid names
            "loanword": "loanword",
            # loanEventTimeDepthBP
            "loanSourceCognateClass_id": "loanSourceCognateClass_id",
            "sourceFormInLoanLanguage": "sourceFormInLoanLanguage",
            # should be put in forms.csv!? (only 509, though)
            "parallelLoanEvent": "parallelLoanEvent",
            # -> if True, split into individual borrowings!

            # notProtoIndoEuropean
            # dubiousSet:                 always True
            # parallelDerivation:         13 True
            # revisedBy
            # revisedYet
            # ideophonic:                 49 True
            # proposedAsCognateTo_id:    110 not-NULL
            # proposedAsCognateToScale
        }
}

"""
meaninglistorder
    id
    meaning_id
    meaning_list_id
    order
*citation
    reliability     A|B|C|X
"""