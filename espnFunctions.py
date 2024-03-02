import requests
import json

def getTeams(url):
    # url = "https://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/teams/?group=50&limit=1000"

    payload = {}
    headers = {
    'authority': 'sports.core.api.espn.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 's_ecid=MCMID%7C82792784420277388583135444684810980743; ESPN-ONESITE.WEB-PROD-ac=XUS; espnAuth={"swid":"{6629E29D-F4D9-42B3-A9E2-9DF4D9E2B394}"}; OptanonAlertBoxClosed=2023-06-22T10:10:24.284Z; eupubconsent-v2=CPtwnzAPtwnzAAcABBENDJCgAAAAAH_AAAYgJgNf_X__b2_r-_7_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF16tqoKuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f__z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-f_87_BMEAkw1LiALsyxwJtowihRAjCsJCqBQAUUAwtEBhA6uCnZXAT6wiQAoBQBOBECHAFGTAIAABIAkIgAkCPBAIAAIBAACABUIhAAxsAgsALAQCAAUB0LFGKAIQJCDIiIiFMCAqRIKCeyoQSg_0NMIQ6ywAoNH_FQgI1kDFYEQkLByHBEgJeLJA9xRvkAIwAoBRKhWopPTQEKGZssAAAAA.YAAAD_gAAAAA; SWID=0F5AB509-C4F2-41FD-C1AD-C0E99A18BFA5; country=us; AMCVS_EE0201AC512D2BE80A490D4C%40AdobeOrg=1; check=true; _omnicwtest=works; _gcl_au=1.1.881177520.1708556575; _ga_H0P43ZY447=GS1.1.1708556576.1.0.1708556576.0.0.0; _ga=GA1.1.158919609.1708556576; dtcAuth=ESPN_PLUS; userZip=27610; s_cc=true; hashedIp=72c14d426bc05fa354795cb4f1cab57de4799a9450cc3d17223b894a8aefbf7d; _cb=3_ERoCNvNWcBXvpWW; IR_gbd=espn.com; _fbp=fb.1.1708556578884.876071017; optimizelyEndUserId=oeu1708876548119ds.0d35c1539a939379; s_omni_lid=%5B%5BB%5D%5D; ESPN-ONESITE.WEB-PROD.token=5=eyJhY2Nlc3NfdG9rZW4iOiIzNjRhYWZhNzA4MWU0NWE1YmY0NDgxN2NmNzhjMjgwMiIsInJlZnJlc2hfdG9rZW4iOiJmNzEwYjQyN2M4M2M0NmM3OWU3ZjU1NDIxODU4OGZjMiIsInN3aWQiOiJ7NjYyOUUyOUQtRjREOS00MkIzLUE5RTItOURGNEQ5RTJCMzk0fSIsInR0bCI6ODY0MDAsInJlZnJlc2hfdHRsIjoxNTU1MjAwMCwiaGlnaF90cnVzdF9leHBpcmVzX2luIjpudWxsLCJpbml0aWFsX2dyYW50X2luX2NoYWluX3RpbWUiOjE2NjAxNzE4MDc5MzcsImlhdCI6MTcwOTAzMTY4MTAwMCwiZXhwIjoxNzA5MTE4MDgxMDAwLCJyZWZyZXNoX2V4cCI6MTcyNDU4MzY4MTAwMCwiaGlnaF90cnVzdF9leHAiOm51bGwsInNzbyI6bnVsbCwiYXV0aGVudGljYXRvciI6ImRpc25leWlkIiwibG9naW5WYWx1ZSI6bnVsbCwiY2xpY2tiYWNrVHlwZSI6bnVsbCwic2Vzc2lvblRyYW5zZmVyS2V5IjoiQl91N1lDbFJKMHdldXJTc3NqZEFMdzRYUmx0ZEJfMGJhWUhQNlRlTmhXOWJyZlJ4TnU1VU5EMlZTWHJSSzRlUWxKYWM0RzM3OWFzVFhxaUE3MXNsbFZzS3g1clNuaTRJSkR2Z1JPeF9SaDNZb2ZJeF8zayIsImNyZWF0ZWQiOiIyMDI0LTAyLTI3VDExOjAxOjIxLjQ0N1oiLCJsYXN0Q2hlY2tlZCI6IjIwMjQtMDItMjdUMTE6MDE6MjEuNDQ3WiIsImV4cGlyZXMiOiIyMDI0LTAyLTI4VDExOjAxOjIxLjAwMFoiLCJyZWZyZXNoX2V4cGlyZXMiOiIyMDI0LTA4LTI1VDExOjAxOjIxLjAwMFoifQ==|eyJraWQiOiJxUEhmditOL0tONE1zYnVwSE1PWWxBc0pLcWVaS1U2Mi9DZjNpSm1uOEJ6dzlwSW5xbTVzUnc9PSIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJodHRwczovL2F1dGhvcml6YXRpb24uZ28uY29tIiwic3ViIjoiezY2MjlFMjlELUY0RDktNDJCMy1BOUUyLTlERjREOUUyQjM5NH0iLCJhdWQiOiJFU1BOLU9ORVNJVEUuV0VCLVBST0QiLCJleHAiOjE3MDkxMTgwODEsImlhdCI6MTcwOTAzMTY4MSwianRpIjoiSzB5NjBNNWFrbTVCb040ZWl0Q2FNdyIsIm5iZiI6MTcwOTAzMTYyMSwiYV90eXAiOiJPTkVJRF9UUlVTVEVEIiwiYV9jYXQiOiJHVUVTVCIsImF0ciI6ImRpc25leWlkIiwic2NvcGVzIjpbIkFVVEhaX0dVRVNUX1NFQ1VSRURfU0VTU0lPTiJdLCJjX3RpZCI6IjEzMjQiLCJpZ2ljIjoxNjYwMTcxODA3OTM3LCJodGF2IjoyLCJodGQiOjE4MDAsInJ0dGwiOjE1NTUyMDAwLCJlbWFpbCI6ImJ3YXR0bGV3b3J0aDhAZ21haWwuY29tIn0.ie5zmNBq7PArejEyKkY9DOT-OjQu1WnITAeG7VTzXTQJ00D3TR5gz558r4M5G37qGtOuPGoMNmRDfG9chBdzUL9LFIK1GDsWAVQL0tnGp-cW7JIWwClXoMDI7tmFmzxxrveFRTO_VAvhuxzSj7WXFWP6zexg0InfByFkw_yKKkw8P5DXizF-zTHY-fAHBg0sin6pEFlcbPI4gfuSnEj0EUOCe-Z7-NmSoSrbvzLQTfZXB0HFea9tt-aLmwdfZ4gBscm1VBuzlM_AXv8-NAQwbXdXCNolsZ0TK87oyG-EaRWjiFSJoojdCnH19tuObshq09aOdbc87aLPUngH_jGKjw; AMCV_EE0201AC512D2BE80A490D4C%40AdobeOrg=-330454231%7CMCIDTS%7C19781%7CMCMID%7C82792784420277388583135444684810980743%7CMCAAMLH-1709675775%7C9%7CMCAAMB-1709675775%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1709078175s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; mbox=PC#54a5125bf17940cbbd7c3deddd32833a.34_0#1772319428|session#72a7af10ee42470a87008556550ba500#1709076488; OptanonConsent=isIABGlobal=false&datestamp=Tue+Feb+27+2024+17%3A57%3A08+GMT-0500+(Eastern+Standard+Time)&version=202309.1.0&hosts=&consentId=60f13863-decd-4d1f-8e81-22d8317b14df&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0005%3A1%2CBG1145%3A1&AwaitingReconsent=false&isGpcEnabled=0&geolocation=GB%3B&browserGpcFlag=0; IR_9070=1709074628169%7C0%7C1709074628169%7C%7C; _chartbeat2=.1660171769681.1709074628209.0000000001100101.DC3zYMB_wgNABB79-KDDW997CtKRwm.1; ab.storage.sessionId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%22aa88c317-e2bc-5ad4-5e48-ce2c04414571%22%2C%22e%22%3A1709076428353%2C%22c%22%3A1709074628354%2C%22l%22%3A1709074628354%7D; ab.storage.deviceId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%22ec416753-70bc-bde7-dbd3-988e7f3397a8%22%2C%22c%22%3A1660171811249%2C%22l%22%3A1709074628355%7D; ab.storage.userId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%220F5AB509-C4F2-41FD-C1AD-C0E99A18BFA5%22%2C%22c%22%3A1708556571958%2C%22l%22%3A1709074628356%7D; s_sq=%5B%5BB%5D%5D; nol_fpid=cxi7kznztrjarpitttsaahwl13aa81708556578|1708556578875|1709074629731|1709074629734; __gads=ID=20733b6ec75f4cf8:T=1708556574:RT=1709074629:S=ALNI_MZ-98Q_Yg-0V6IkaSrgEfNc-_fu_w; __gpi=UID=00000dcbf9558565:T=1708556574:RT=1709074629:S=ALNI_MZ20-dIjllfqeeLcE6tuvupMVktkg; __eoi=ID=eea71bac2273bdf3:T=1708556574:RT=1709074629:S=AA-Afjbpob73THfUBJGxC4YuKKQP; s_c24=1709074630078; s_c6=1709074630081-Repeat; espn_s2=AEBwSeYYhL5Ech4na648EHgtXnn%2BKKB0tKg0Zxc1Lm1wT0CCUseiWtcVsYV%2FYLAkIustDCZAUsJK3wqm1OazVA%2FHq03x00Wly%2BzwYRk6KBAKxKwPIYAvXasvCkww3FbeBfmxaIRI16aWpHz2LR58PNtgmazeSKoNRNk6iioZ6CCf4xCyGABBjOENt6KtQTl25XteliznFnSVAV99%2B8yY5f4xDcHuWCJeVVqzLHCTHPhseSlqEWkKgGluQ3xSw85690Wx9OMHzWU2sC8xSwyGkVfxSFDmr7cpIb7T3h8ebyivMA%3D%3D; ESPN-ONESITE.WEB-PROD.idn=001ad3796b; FCNEC=%5B%5B%22AKsRol_Fe5S3crsVUKY9sUwfS6fZpW2viVobBmPAf9Fheuu9PfMRni1Kz0FbttJ4sOlMyoqvGJSBDxsV4-9-uqHyAHuCrlcPMclpAepS9kSx9QB2UUbpId_uPiBHqnUh8RgdyVDfwA3W922GYJUmYIpj5-MrmSflAw%3D%3D%22%5D%5D',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    items = data['items']

    teams = []
    team_count = 0
    for item in items:
        url = item['$ref']
        response = requests.request("GET", url, headers=headers, data=payload)
        teams.append(response.json())
        team_count += 1

    content = json.dumps(teams)
    content = content.replace('$ref', 'ref')

    f = open('teams.json', 'w')
    f.write(content)
    f.close()
    return(f"Wrote {team_count} NCAAB Division 1 teams to teams.json")

def getRoster(team, url):
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams/1/roster"

    payload = {}
    headers = {
    'authority': 'site.api.espn.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 's_ecid=MCMID%7C82792784420277388583135444684810980743; ESPN-ONESITE.WEB-PROD-ac=XUS; espnAuth={"swid":"{6629E29D-F4D9-42B3-A9E2-9DF4D9E2B394}"}; OptanonAlertBoxClosed=2023-06-22T10:10:24.284Z; eupubconsent-v2=CPtwnzAPtwnzAAcABBENDJCgAAAAAH_AAAYgJgNf_X__b2_r-_7_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF16tqoKuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f__z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-f_87_BMEAkw1LiALsyxwJtowihRAjCsJCqBQAUUAwtEBhA6uCnZXAT6wiQAoBQBOBECHAFGTAIAABIAkIgAkCPBAIAAIBAACABUIhAAxsAgsALAQCAAUB0LFGKAIQJCDIiIiFMCAqRIKCeyoQSg_0NMIQ6ywAoNH_FQgI1kDFYEQkLByHBEgJeLJA9xRvkAIwAoBRKhWopPTQEKGZssAAAAA.YAAAD_gAAAAA; SWID=0F5AB509-C4F2-41FD-C1AD-C0E99A18BFA5; country=us; AMCVS_EE0201AC512D2BE80A490D4C%40AdobeOrg=1; check=true; _omnicwtest=works; _gcl_au=1.1.881177520.1708556575; _ga_H0P43ZY447=GS1.1.1708556576.1.0.1708556576.0.0.0; _ga=GA1.1.158919609.1708556576; dtcAuth=ESPN_PLUS; userZip=27610; s_cc=true; hashedIp=72c14d426bc05fa354795cb4f1cab57de4799a9450cc3d17223b894a8aefbf7d; _cb=3_ERoCNvNWcBXvpWW; IR_gbd=espn.com; _fbp=fb.1.1708556578884.876071017; optimizelyEndUserId=oeu1708876548119ds.0d35c1539a939379; s_omni_lid=%5B%5BB%5D%5D; ESPN-ONESITE.WEB-PROD.token=5=eyJhY2Nlc3NfdG9rZW4iOiIzNjRhYWZhNzA4MWU0NWE1YmY0NDgxN2NmNzhjMjgwMiIsInJlZnJlc2hfdG9rZW4iOiJmNzEwYjQyN2M4M2M0NmM3OWU3ZjU1NDIxODU4OGZjMiIsInN3aWQiOiJ7NjYyOUUyOUQtRjREOS00MkIzLUE5RTItOURGNEQ5RTJCMzk0fSIsInR0bCI6ODY0MDAsInJlZnJlc2hfdHRsIjoxNTU1MjAwMCwiaGlnaF90cnVzdF9leHBpcmVzX2luIjpudWxsLCJpbml0aWFsX2dyYW50X2luX2NoYWluX3RpbWUiOjE2NjAxNzE4MDc5MzcsImlhdCI6MTcwOTAzMTY4MTAwMCwiZXhwIjoxNzA5MTE4MDgxMDAwLCJyZWZyZXNoX2V4cCI6MTcyNDU4MzY4MTAwMCwiaGlnaF90cnVzdF9leHAiOm51bGwsInNzbyI6bnVsbCwiYXV0aGVudGljYXRvciI6ImRpc25leWlkIiwibG9naW5WYWx1ZSI6bnVsbCwiY2xpY2tiYWNrVHlwZSI6bnVsbCwic2Vzc2lvblRyYW5zZmVyS2V5IjoiQl91N1lDbFJKMHdldXJTc3NqZEFMdzRYUmx0ZEJfMGJhWUhQNlRlTmhXOWJyZlJ4TnU1VU5EMlZTWHJSSzRlUWxKYWM0RzM3OWFzVFhxaUE3MXNsbFZzS3g1clNuaTRJSkR2Z1JPeF9SaDNZb2ZJeF8zayIsImNyZWF0ZWQiOiIyMDI0LTAyLTI3VDExOjAxOjIxLjQ0N1oiLCJsYXN0Q2hlY2tlZCI6IjIwMjQtMDItMjdUMTE6MDE6MjEuNDQ3WiIsImV4cGlyZXMiOiIyMDI0LTAyLTI4VDExOjAxOjIxLjAwMFoiLCJyZWZyZXNoX2V4cGlyZXMiOiIyMDI0LTA4LTI1VDExOjAxOjIxLjAwMFoifQ==|eyJraWQiOiJxUEhmditOL0tONE1zYnVwSE1PWWxBc0pLcWVaS1U2Mi9DZjNpSm1uOEJ6dzlwSW5xbTVzUnc9PSIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJodHRwczovL2F1dGhvcml6YXRpb24uZ28uY29tIiwic3ViIjoiezY2MjlFMjlELUY0RDktNDJCMy1BOUUyLTlERjREOUUyQjM5NH0iLCJhdWQiOiJFU1BOLU9ORVNJVEUuV0VCLVBST0QiLCJleHAiOjE3MDkxMTgwODEsImlhdCI6MTcwOTAzMTY4MSwianRpIjoiSzB5NjBNNWFrbTVCb040ZWl0Q2FNdyIsIm5iZiI6MTcwOTAzMTYyMSwiYV90eXAiOiJPTkVJRF9UUlVTVEVEIiwiYV9jYXQiOiJHVUVTVCIsImF0ciI6ImRpc25leWlkIiwic2NvcGVzIjpbIkFVVEhaX0dVRVNUX1NFQ1VSRURfU0VTU0lPTiJdLCJjX3RpZCI6IjEzMjQiLCJpZ2ljIjoxNjYwMTcxODA3OTM3LCJodGF2IjoyLCJodGQiOjE4MDAsInJ0dGwiOjE1NTUyMDAwLCJlbWFpbCI6ImJ3YXR0bGV3b3J0aDhAZ21haWwuY29tIn0.ie5zmNBq7PArejEyKkY9DOT-OjQu1WnITAeG7VTzXTQJ00D3TR5gz558r4M5G37qGtOuPGoMNmRDfG9chBdzUL9LFIK1GDsWAVQL0tnGp-cW7JIWwClXoMDI7tmFmzxxrveFRTO_VAvhuxzSj7WXFWP6zexg0InfByFkw_yKKkw8P5DXizF-zTHY-fAHBg0sin6pEFlcbPI4gfuSnEj0EUOCe-Z7-NmSoSrbvzLQTfZXB0HFea9tt-aLmwdfZ4gBscm1VBuzlM_AXv8-NAQwbXdXCNolsZ0TK87oyG-EaRWjiFSJoojdCnH19tuObshq09aOdbc87aLPUngH_jGKjw; AMCV_EE0201AC512D2BE80A490D4C%40AdobeOrg=-330454231%7CMCIDTS%7C19781%7CMCMID%7C82792784420277388583135444684810980743%7CMCAAMLH-1709675775%7C9%7CMCAAMB-1709675775%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1709078175s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; mbox=PC#54a5125bf17940cbbd7c3deddd32833a.34_0#1772319428|session#72a7af10ee42470a87008556550ba500#1709076488; OptanonConsent=isIABGlobal=false&datestamp=Tue+Feb+27+2024+17%3A57%3A08+GMT-0500+(Eastern+Standard+Time)&version=202309.1.0&hosts=&consentId=60f13863-decd-4d1f-8e81-22d8317b14df&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0005%3A1%2CBG1145%3A1&AwaitingReconsent=false&isGpcEnabled=0&geolocation=GB%3B&browserGpcFlag=0; IR_9070=1709074628169%7C0%7C1709074628169%7C%7C; _chartbeat2=.1660171769681.1709074628209.0000000001100101.DC3zYMB_wgNABB79-KDDW997CtKRwm.1; ab.storage.sessionId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%22aa88c317-e2bc-5ad4-5e48-ce2c04414571%22%2C%22e%22%3A1709076428353%2C%22c%22%3A1709074628354%2C%22l%22%3A1709074628354%7D; ab.storage.deviceId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%22ec416753-70bc-bde7-dbd3-988e7f3397a8%22%2C%22c%22%3A1660171811249%2C%22l%22%3A1709074628355%7D; ab.storage.userId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%220F5AB509-C4F2-41FD-C1AD-C0E99A18BFA5%22%2C%22c%22%3A1708556571958%2C%22l%22%3A1709074628356%7D; s_sq=%5B%5BB%5D%5D; nol_fpid=cxi7kznztrjarpitttsaahwl13aa81708556578|1708556578875|1709074629731|1709074629734; __gads=ID=20733b6ec75f4cf8:T=1708556574:RT=1709074629:S=ALNI_MZ-98Q_Yg-0V6IkaSrgEfNc-_fu_w; __gpi=UID=00000dcbf9558565:T=1708556574:RT=1709074629:S=ALNI_MZ20-dIjllfqeeLcE6tuvupMVktkg; __eoi=ID=eea71bac2273bdf3:T=1708556574:RT=1709074629:S=AA-Afjbpob73THfUBJGxC4YuKKQP; s_c24=1709074630078; s_c6=1709074630081-Repeat; espn_s2=AEBwSeYYhL5Ech4na648EHgtXnn%2BKKB0tKg0Zxc1Lm1wT0CCUseiWtcVsYV%2FYLAkIustDCZAUsJK3wqm1OazVA%2FHq03x00Wly%2BzwYRk6KBAKxKwPIYAvXasvCkww3FbeBfmxaIRI16aWpHz2LR58PNtgmazeSKoNRNk6iioZ6CCf4xCyGABBjOENt6KtQTl25XteliznFnSVAV99%2B8yY5f4xDcHuWCJeVVqzLHCTHPhseSlqEWkKgGluQ3xSw85690Wx9OMHzWU2sC8xSwyGkVfxSFDmr7cpIb7T3h8ebyivMA%3D%3D; ESPN-ONESITE.WEB-PROD.idn=001ad3796b; FCNEC=%5B%5B%22AKsRol_Fe5S3crsVUKY9sUwfS6fZpW2viVobBmPAf9Fheuu9PfMRni1Kz0FbttJ4sOlMyoqvGJSBDxsV4-9-uqHyAHuCrlcPMclpAepS9kSx9QB2UUbpId_uPiBHqnUh8RgdyVDfwA3W922GYJUmYIpj5-MrmSflAw%3D%3D%22%5D%5D',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    content = json.dumps(data)

    f = open(f'rosters/{team}.json', 'w')
    f.write(content)
    f.close()
    return(f"Roster updated for {team}")

def getPlayers(url):
    # url = http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2024/athletes?lang=en&region=us&limit=1000
    
    payload = {}
    headers = {
    'authority': 'sports.core.api.espn.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 's_ecid=MCMID%7C82792784420277388583135444684810980743; ESPN-ONESITE.WEB-PROD-ac=XUS; espnAuth={"swid":"{6629E29D-F4D9-42B3-A9E2-9DF4D9E2B394}"}; OptanonAlertBoxClosed=2023-06-22T10:10:24.284Z; eupubconsent-v2=CPtwnzAPtwnzAAcABBENDJCgAAAAAH_AAAYgJgNf_X__b2_r-_7_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF16tqoKuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f__z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-f_87_BMEAkw1LiALsyxwJtowihRAjCsJCqBQAUUAwtEBhA6uCnZXAT6wiQAoBQBOBECHAFGTAIAABIAkIgAkCPBAIAAIBAACABUIhAAxsAgsALAQCAAUB0LFGKAIQJCDIiIiFMCAqRIKCeyoQSg_0NMIQ6ywAoNH_FQgI1kDFYEQkLByHBEgJeLJA9xRvkAIwAoBRKhWopPTQEKGZssAAAAA.YAAAD_gAAAAA; SWID=0F5AB509-C4F2-41FD-C1AD-C0E99A18BFA5; country=us; AMCVS_EE0201AC512D2BE80A490D4C%40AdobeOrg=1; check=true; _omnicwtest=works; _gcl_au=1.1.881177520.1708556575; _ga_H0P43ZY447=GS1.1.1708556576.1.0.1708556576.0.0.0; _ga=GA1.1.158919609.1708556576; dtcAuth=ESPN_PLUS; userZip=27610; s_cc=true; hashedIp=72c14d426bc05fa354795cb4f1cab57de4799a9450cc3d17223b894a8aefbf7d; _cb=3_ERoCNvNWcBXvpWW; IR_gbd=espn.com; _fbp=fb.1.1708556578884.876071017; optimizelyEndUserId=oeu1708876548119ds.0d35c1539a939379; s_omni_lid=%5B%5BB%5D%5D; ESPN-ONESITE.WEB-PROD.token=5=eyJhY2Nlc3NfdG9rZW4iOiIzNjRhYWZhNzA4MWU0NWE1YmY0NDgxN2NmNzhjMjgwMiIsInJlZnJlc2hfdG9rZW4iOiJmNzEwYjQyN2M4M2M0NmM3OWU3ZjU1NDIxODU4OGZjMiIsInN3aWQiOiJ7NjYyOUUyOUQtRjREOS00MkIzLUE5RTItOURGNEQ5RTJCMzk0fSIsInR0bCI6ODY0MDAsInJlZnJlc2hfdHRsIjoxNTU1MjAwMCwiaGlnaF90cnVzdF9leHBpcmVzX2luIjpudWxsLCJpbml0aWFsX2dyYW50X2luX2NoYWluX3RpbWUiOjE2NjAxNzE4MDc5MzcsImlhdCI6MTcwOTAzMTY4MTAwMCwiZXhwIjoxNzA5MTE4MDgxMDAwLCJyZWZyZXNoX2V4cCI6MTcyNDU4MzY4MTAwMCwiaGlnaF90cnVzdF9leHAiOm51bGwsInNzbyI6bnVsbCwiYXV0aGVudGljYXRvciI6ImRpc25leWlkIiwibG9naW5WYWx1ZSI6bnVsbCwiY2xpY2tiYWNrVHlwZSI6bnVsbCwic2Vzc2lvblRyYW5zZmVyS2V5IjoiQl91N1lDbFJKMHdldXJTc3NqZEFMdzRYUmx0ZEJfMGJhWUhQNlRlTmhXOWJyZlJ4TnU1VU5EMlZTWHJSSzRlUWxKYWM0RzM3OWFzVFhxaUE3MXNsbFZzS3g1clNuaTRJSkR2Z1JPeF9SaDNZb2ZJeF8zayIsImNyZWF0ZWQiOiIyMDI0LTAyLTI3VDExOjAxOjIxLjQ0N1oiLCJsYXN0Q2hlY2tlZCI6IjIwMjQtMDItMjdUMTE6MDE6MjEuNDQ3WiIsImV4cGlyZXMiOiIyMDI0LTAyLTI4VDExOjAxOjIxLjAwMFoiLCJyZWZyZXNoX2V4cGlyZXMiOiIyMDI0LTA4LTI1VDExOjAxOjIxLjAwMFoifQ==|eyJraWQiOiJxUEhmditOL0tONE1zYnVwSE1PWWxBc0pLcWVaS1U2Mi9DZjNpSm1uOEJ6dzlwSW5xbTVzUnc9PSIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJodHRwczovL2F1dGhvcml6YXRpb24uZ28uY29tIiwic3ViIjoiezY2MjlFMjlELUY0RDktNDJCMy1BOUUyLTlERjREOUUyQjM5NH0iLCJhdWQiOiJFU1BOLU9ORVNJVEUuV0VCLVBST0QiLCJleHAiOjE3MDkxMTgwODEsImlhdCI6MTcwOTAzMTY4MSwianRpIjoiSzB5NjBNNWFrbTVCb040ZWl0Q2FNdyIsIm5iZiI6MTcwOTAzMTYyMSwiYV90eXAiOiJPTkVJRF9UUlVTVEVEIiwiYV9jYXQiOiJHVUVTVCIsImF0ciI6ImRpc25leWlkIiwic2NvcGVzIjpbIkFVVEhaX0dVRVNUX1NFQ1VSRURfU0VTU0lPTiJdLCJjX3RpZCI6IjEzMjQiLCJpZ2ljIjoxNjYwMTcxODA3OTM3LCJodGF2IjoyLCJodGQiOjE4MDAsInJ0dGwiOjE1NTUyMDAwLCJlbWFpbCI6ImJ3YXR0bGV3b3J0aDhAZ21haWwuY29tIn0.ie5zmNBq7PArejEyKkY9DOT-OjQu1WnITAeG7VTzXTQJ00D3TR5gz558r4M5G37qGtOuPGoMNmRDfG9chBdzUL9LFIK1GDsWAVQL0tnGp-cW7JIWwClXoMDI7tmFmzxxrveFRTO_VAvhuxzSj7WXFWP6zexg0InfByFkw_yKKkw8P5DXizF-zTHY-fAHBg0sin6pEFlcbPI4gfuSnEj0EUOCe-Z7-NmSoSrbvzLQTfZXB0HFea9tt-aLmwdfZ4gBscm1VBuzlM_AXv8-NAQwbXdXCNolsZ0TK87oyG-EaRWjiFSJoojdCnH19tuObshq09aOdbc87aLPUngH_jGKjw; AMCV_EE0201AC512D2BE80A490D4C%40AdobeOrg=-330454231%7CMCIDTS%7C19781%7CMCMID%7C82792784420277388583135444684810980743%7CMCAAMLH-1709675775%7C9%7CMCAAMB-1709675775%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1709078175s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; mbox=PC#54a5125bf17940cbbd7c3deddd32833a.34_0#1772319428|session#72a7af10ee42470a87008556550ba500#1709076488; OptanonConsent=isIABGlobal=false&datestamp=Tue+Feb+27+2024+17%3A57%3A08+GMT-0500+(Eastern+Standard+Time)&version=202309.1.0&hosts=&consentId=60f13863-decd-4d1f-8e81-22d8317b14df&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0005%3A1%2CBG1145%3A1&AwaitingReconsent=false&isGpcEnabled=0&geolocation=GB%3B&browserGpcFlag=0; IR_9070=1709074628169%7C0%7C1709074628169%7C%7C; _chartbeat2=.1660171769681.1709074628209.0000000001100101.DC3zYMB_wgNABB79-KDDW997CtKRwm.1; ab.storage.sessionId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%22aa88c317-e2bc-5ad4-5e48-ce2c04414571%22%2C%22e%22%3A1709076428353%2C%22c%22%3A1709074628354%2C%22l%22%3A1709074628354%7D; ab.storage.deviceId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%22ec416753-70bc-bde7-dbd3-988e7f3397a8%22%2C%22c%22%3A1660171811249%2C%22l%22%3A1709074628355%7D; ab.storage.userId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%220F5AB509-C4F2-41FD-C1AD-C0E99A18BFA5%22%2C%22c%22%3A1708556571958%2C%22l%22%3A1709074628356%7D; s_sq=%5B%5BB%5D%5D; nol_fpid=cxi7kznztrjarpitttsaahwl13aa81708556578|1708556578875|1709074629731|1709074629734; __gads=ID=20733b6ec75f4cf8:T=1708556574:RT=1709074629:S=ALNI_MZ-98Q_Yg-0V6IkaSrgEfNc-_fu_w; __gpi=UID=00000dcbf9558565:T=1708556574:RT=1709074629:S=ALNI_MZ20-dIjllfqeeLcE6tuvupMVktkg; __eoi=ID=eea71bac2273bdf3:T=1708556574:RT=1709074629:S=AA-Afjbpob73THfUBJGxC4YuKKQP; s_c24=1709074630078; s_c6=1709074630081-Repeat; espn_s2=AEBwSeYYhL5Ech4na648EHgtXnn%2BKKB0tKg0Zxc1Lm1wT0CCUseiWtcVsYV%2FYLAkIustDCZAUsJK3wqm1OazVA%2FHq03x00Wly%2BzwYRk6KBAKxKwPIYAvXasvCkww3FbeBfmxaIRI16aWpHz2LR58PNtgmazeSKoNRNk6iioZ6CCf4xCyGABBjOENt6KtQTl25XteliznFnSVAV99%2B8yY5f4xDcHuWCJeVVqzLHCTHPhseSlqEWkKgGluQ3xSw85690Wx9OMHzWU2sC8xSwyGkVfxSFDmr7cpIb7T3h8ebyivMA%3D%3D; ESPN-ONESITE.WEB-PROD.idn=001ad3796b; FCNEC=%5B%5B%22AKsRol_Fe5S3crsVUKY9sUwfS6fZpW2viVobBmPAf9Fheuu9PfMRni1Kz0FbttJ4sOlMyoqvGJSBDxsV4-9-uqHyAHuCrlcPMclpAepS9kSx9QB2UUbpId_uPiBHqnUh8RgdyVDfwA3W922GYJUmYIpj5-MrmSflAw%3D%3D%22%5D%5D',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    # The number of total athletes (records) available
    recordsCount = data['count']
    # The index of the current page
    pageIndex = data['pageIndex']
    # The number of athletes (records) on current page
    pageSize = data['pageSize']
    # The number of total pages of athletes (records)
    pageCount = data['pageCount']
    # The list of athletes on current page
    athletes = data['items']

    content = [json.dumps(athletes)]

    while pageIndex < pageCount:
        response = requests.request("GET", url, headers=headers, data=payload)
        pageIndex = data['pageIndex']
        pageCount = data['pageCount']
        athletes = data['items']
        content.append(json.dumps(athletes))

    #
    # Need to finish, above has looped through all given athletes and added to a List of dicts
    # Need to now write these to files, 1 file per athlete or 1 file with all athletes??
    #
            
    f = open(f'playerStats/{id}.json', 'w')
    f.write(content)
    f.close()

def getPlayerStats(id, stats_url):
    # url = "https://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2024/types/0/athletes/4433176/statistics"

    payload = {}
    headers = {
    'authority': 'sports.core.api.espn.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 's_ecid=MCMID%7C82792784420277388583135444684810980743; ESPN-ONESITE.WEB-PROD-ac=XUS; espnAuth={"swid":"{6629E29D-F4D9-42B3-A9E2-9DF4D9E2B394}"}; OptanonAlertBoxClosed=2023-06-22T10:10:24.284Z; eupubconsent-v2=CPtwnzAPtwnzAAcABBENDJCgAAAAAH_AAAYgJgNf_X__b2_r-_7_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF16tqoKuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f__z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-f_87_BMEAkw1LiALsyxwJtowihRAjCsJCqBQAUUAwtEBhA6uCnZXAT6wiQAoBQBOBECHAFGTAIAABIAkIgAkCPBAIAAIBAACABUIhAAxsAgsALAQCAAUB0LFGKAIQJCDIiIiFMCAqRIKCeyoQSg_0NMIQ6ywAoNH_FQgI1kDFYEQkLByHBEgJeLJA9xRvkAIwAoBRKhWopPTQEKGZssAAAAA.YAAAD_gAAAAA; SWID=0F5AB509-C4F2-41FD-C1AD-C0E99A18BFA5; country=us; AMCVS_EE0201AC512D2BE80A490D4C%40AdobeOrg=1; check=true; _omnicwtest=works; _gcl_au=1.1.881177520.1708556575; _ga_H0P43ZY447=GS1.1.1708556576.1.0.1708556576.0.0.0; _ga=GA1.1.158919609.1708556576; dtcAuth=ESPN_PLUS; userZip=27610; s_cc=true; hashedIp=72c14d426bc05fa354795cb4f1cab57de4799a9450cc3d17223b894a8aefbf7d; _cb=3_ERoCNvNWcBXvpWW; IR_gbd=espn.com; _fbp=fb.1.1708556578884.876071017; optimizelyEndUserId=oeu1708876548119ds.0d35c1539a939379; s_omni_lid=%5B%5BB%5D%5D; ESPN-ONESITE.WEB-PROD.token=5=eyJhY2Nlc3NfdG9rZW4iOiIzNjRhYWZhNzA4MWU0NWE1YmY0NDgxN2NmNzhjMjgwMiIsInJlZnJlc2hfdG9rZW4iOiJmNzEwYjQyN2M4M2M0NmM3OWU3ZjU1NDIxODU4OGZjMiIsInN3aWQiOiJ7NjYyOUUyOUQtRjREOS00MkIzLUE5RTItOURGNEQ5RTJCMzk0fSIsInR0bCI6ODY0MDAsInJlZnJlc2hfdHRsIjoxNTU1MjAwMCwiaGlnaF90cnVzdF9leHBpcmVzX2luIjpudWxsLCJpbml0aWFsX2dyYW50X2luX2NoYWluX3RpbWUiOjE2NjAxNzE4MDc5MzcsImlhdCI6MTcwOTAzMTY4MTAwMCwiZXhwIjoxNzA5MTE4MDgxMDAwLCJyZWZyZXNoX2V4cCI6MTcyNDU4MzY4MTAwMCwiaGlnaF90cnVzdF9leHAiOm51bGwsInNzbyI6bnVsbCwiYXV0aGVudGljYXRvciI6ImRpc25leWlkIiwibG9naW5WYWx1ZSI6bnVsbCwiY2xpY2tiYWNrVHlwZSI6bnVsbCwic2Vzc2lvblRyYW5zZmVyS2V5IjoiQl91N1lDbFJKMHdldXJTc3NqZEFMdzRYUmx0ZEJfMGJhWUhQNlRlTmhXOWJyZlJ4TnU1VU5EMlZTWHJSSzRlUWxKYWM0RzM3OWFzVFhxaUE3MXNsbFZzS3g1clNuaTRJSkR2Z1JPeF9SaDNZb2ZJeF8zayIsImNyZWF0ZWQiOiIyMDI0LTAyLTI3VDExOjAxOjIxLjQ0N1oiLCJsYXN0Q2hlY2tlZCI6IjIwMjQtMDItMjdUMTE6MDE6MjEuNDQ3WiIsImV4cGlyZXMiOiIyMDI0LTAyLTI4VDExOjAxOjIxLjAwMFoiLCJyZWZyZXNoX2V4cGlyZXMiOiIyMDI0LTA4LTI1VDExOjAxOjIxLjAwMFoifQ==|eyJraWQiOiJxUEhmditOL0tONE1zYnVwSE1PWWxBc0pLcWVaS1U2Mi9DZjNpSm1uOEJ6dzlwSW5xbTVzUnc9PSIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJodHRwczovL2F1dGhvcml6YXRpb24uZ28uY29tIiwic3ViIjoiezY2MjlFMjlELUY0RDktNDJCMy1BOUUyLTlERjREOUUyQjM5NH0iLCJhdWQiOiJFU1BOLU9ORVNJVEUuV0VCLVBST0QiLCJleHAiOjE3MDkxMTgwODEsImlhdCI6MTcwOTAzMTY4MSwianRpIjoiSzB5NjBNNWFrbTVCb040ZWl0Q2FNdyIsIm5iZiI6MTcwOTAzMTYyMSwiYV90eXAiOiJPTkVJRF9UUlVTVEVEIiwiYV9jYXQiOiJHVUVTVCIsImF0ciI6ImRpc25leWlkIiwic2NvcGVzIjpbIkFVVEhaX0dVRVNUX1NFQ1VSRURfU0VTU0lPTiJdLCJjX3RpZCI6IjEzMjQiLCJpZ2ljIjoxNjYwMTcxODA3OTM3LCJodGF2IjoyLCJodGQiOjE4MDAsInJ0dGwiOjE1NTUyMDAwLCJlbWFpbCI6ImJ3YXR0bGV3b3J0aDhAZ21haWwuY29tIn0.ie5zmNBq7PArejEyKkY9DOT-OjQu1WnITAeG7VTzXTQJ00D3TR5gz558r4M5G37qGtOuPGoMNmRDfG9chBdzUL9LFIK1GDsWAVQL0tnGp-cW7JIWwClXoMDI7tmFmzxxrveFRTO_VAvhuxzSj7WXFWP6zexg0InfByFkw_yKKkw8P5DXizF-zTHY-fAHBg0sin6pEFlcbPI4gfuSnEj0EUOCe-Z7-NmSoSrbvzLQTfZXB0HFea9tt-aLmwdfZ4gBscm1VBuzlM_AXv8-NAQwbXdXCNolsZ0TK87oyG-EaRWjiFSJoojdCnH19tuObshq09aOdbc87aLPUngH_jGKjw; AMCV_EE0201AC512D2BE80A490D4C%40AdobeOrg=-330454231%7CMCIDTS%7C19781%7CMCMID%7C82792784420277388583135444684810980743%7CMCAAMLH-1709675775%7C9%7CMCAAMB-1709675775%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1709078175s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; mbox=PC#54a5125bf17940cbbd7c3deddd32833a.34_0#1772319428|session#72a7af10ee42470a87008556550ba500#1709076488; OptanonConsent=isIABGlobal=false&datestamp=Tue+Feb+27+2024+17%3A57%3A08+GMT-0500+(Eastern+Standard+Time)&version=202309.1.0&hosts=&consentId=60f13863-decd-4d1f-8e81-22d8317b14df&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0005%3A1%2CBG1145%3A1&AwaitingReconsent=false&isGpcEnabled=0&geolocation=GB%3B&browserGpcFlag=0; IR_9070=1709074628169%7C0%7C1709074628169%7C%7C; _chartbeat2=.1660171769681.1709074628209.0000000001100101.DC3zYMB_wgNABB79-KDDW997CtKRwm.1; ab.storage.sessionId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%22aa88c317-e2bc-5ad4-5e48-ce2c04414571%22%2C%22e%22%3A1709076428353%2C%22c%22%3A1709074628354%2C%22l%22%3A1709074628354%7D; ab.storage.deviceId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%22ec416753-70bc-bde7-dbd3-988e7f3397a8%22%2C%22c%22%3A1660171811249%2C%22l%22%3A1709074628355%7D; ab.storage.userId.96ad02b7-2edc-4238-8442-bc35ba85853c=%7B%22g%22%3A%220F5AB509-C4F2-41FD-C1AD-C0E99A18BFA5%22%2C%22c%22%3A1708556571958%2C%22l%22%3A1709074628356%7D; s_sq=%5B%5BB%5D%5D; nol_fpid=cxi7kznztrjarpitttsaahwl13aa81708556578|1708556578875|1709074629731|1709074629734; __gads=ID=20733b6ec75f4cf8:T=1708556574:RT=1709074629:S=ALNI_MZ-98Q_Yg-0V6IkaSrgEfNc-_fu_w; __gpi=UID=00000dcbf9558565:T=1708556574:RT=1709074629:S=ALNI_MZ20-dIjllfqeeLcE6tuvupMVktkg; __eoi=ID=eea71bac2273bdf3:T=1708556574:RT=1709074629:S=AA-Afjbpob73THfUBJGxC4YuKKQP; s_c24=1709074630078; s_c6=1709074630081-Repeat; espn_s2=AEBwSeYYhL5Ech4na648EHgtXnn%2BKKB0tKg0Zxc1Lm1wT0CCUseiWtcVsYV%2FYLAkIustDCZAUsJK3wqm1OazVA%2FHq03x00Wly%2BzwYRk6KBAKxKwPIYAvXasvCkww3FbeBfmxaIRI16aWpHz2LR58PNtgmazeSKoNRNk6iioZ6CCf4xCyGABBjOENt6KtQTl25XteliznFnSVAV99%2B8yY5f4xDcHuWCJeVVqzLHCTHPhseSlqEWkKgGluQ3xSw85690Wx9OMHzWU2sC8xSwyGkVfxSFDmr7cpIb7T3h8ebyivMA%3D%3D; ESPN-ONESITE.WEB-PROD.idn=001ad3796b; FCNEC=%5B%5B%22AKsRol_Fe5S3crsVUKY9sUwfS6fZpW2viVobBmPAf9Fheuu9PfMRni1Kz0FbttJ4sOlMyoqvGJSBDxsV4-9-uqHyAHuCrlcPMclpAepS9kSx9QB2UUbpId_uPiBHqnUh8RgdyVDfwA3W922GYJUmYIpj5-MrmSflAw%3D%3D%22%5D%5D',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", stats_url, headers=headers, data=payload)

    data = response.json()

    content = json.dumps(data)

    f = open(f'playerStats/{id}.json', 'w')
    f.write(content)
    f.close()
    return(f"Player stats updated for player: {id}")
