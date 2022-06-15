from typing import List

import requests
from bs4 import BeautifulSoup


class SpiderUtils:
    BASE_URL = "https://recipe.rakuten.co.jp"

    def __init__(self) -> None:
        pass

    def get_start_urls(self) -> List[str]:
        """クローリングを開始するURLを取得する関数

        Returns:
            start_urls: クローリングを開始するURL
        """
        # url = "https://recipe.rakuten.co.jp/category/"
        # soup = BeautifulSoup(requests.get(url).text, "html.parser")

        # crawled_urls = soup.find_all("a", class_="category_top-list__link")

        # start_urls = [
        #     self.BASE_URL + crawled_url["href"] for crawled_url in crawled_urls
        # ]

        start_urls = [
            "https://recipe.rakuten.co.jp/category/32-338/",
            "https://recipe.rakuten.co.jp/category/32-339/",
            "https://recipe.rakuten.co.jp/category/32-340/",
            "https://recipe.rakuten.co.jp/category/32-341/",
        ]

        return start_urls


"""
'https://recipe.rakuten.co.jp/category/30-300/',
'https://recipe.rakuten.co.jp/category/30-301/',
'https://recipe.rakuten.co.jp/category/30-302/',
'https://recipe.rakuten.co.jp/category/30-307/',
'https://recipe.rakuten.co.jp/category/30-303/',
'https://recipe.rakuten.co.jp/category/30-304/',
'https://recipe.rakuten.co.jp/category/30-305/',
'https://recipe.rakuten.co.jp/category/30-306/',
'https://recipe.rakuten.co.jp/category/30-309/',
'https://recipe.rakuten.co.jp/category/30-310/',
'https://recipe.rakuten.co.jp/category/30-308/',
'https://recipe.rakuten.co.jp/category/30-311/',
'https://recipe.rakuten.co.jp/category/30-312/',
'https://recipe.rakuten.co.jp/category/30-313/',
ここは上手く出来ていない可能性が高い(14~18)
'https://recipe.rakuten.co.jp/category/30-314/',
'https://recipe.rakuten.co.jp/category/30-315/',
'https://recipe.rakuten.co.jp/category/30-316/',
'https://recipe.rakuten.co.jp/category/30-317/',
'https://recipe.rakuten.co.jp/category/30-717/',
'https://recipe.rakuten.co.jp/category/31-318/',
'https://recipe.rakuten.co.jp/category/31-319/',
'https://recipe.rakuten.co.jp/category/31-320/',
'https://recipe.rakuten.co.jp/category/31-321/',
'https://recipe.rakuten.co.jp/category/31-323/',
'https://recipe.rakuten.co.jp/category/31-324/',
'https://recipe.rakuten.co.jp/category/31-325/',
'https://recipe.rakuten.co.jp/category/31-326/',
'https://recipe.rakuten.co.jp/category/31-327/',
'https://recipe.rakuten.co.jp/category/31-328/',
'https://recipe.rakuten.co.jp/category/31-329/',
'https://recipe.rakuten.co.jp/category/31-330/',
'https://recipe.rakuten.co.jp/category/31-331/',
'https://recipe.rakuten.co.jp/category/31-332/',
'https://recipe.rakuten.co.jp/category/31-333/',
'https://recipe.rakuten.co.jp/category/31-334/',
'https://recipe.rakuten.co.jp/category/31-322/',
'https://recipe.rakuten.co.jp/category/31-335/',
'https://recipe.rakuten.co.jp/category/31-718/',
'https://recipe.rakuten.co.jp/category/31-719/',
'https://recipe.rakuten.co.jp/category/31-720/',
'https://recipe.rakuten.co.jp/category/32-336/',
'https://recipe.rakuten.co.jp/category/32-337/',

'https://recipe.rakuten.co.jp/category/32-338/',
'https://recipe.rakuten.co.jp/category/32-339/',
'https://recipe.rakuten.co.jp/category/32-340/',
'https://recipe.rakuten.co.jp/category/32-341/',

'https://recipe.rakuten.co.jp/category/32-342/',
'https://recipe.rakuten.co.jp/category/32-343/',
'https://recipe.rakuten.co.jp/category/32-344/',
'https://recipe.rakuten.co.jp/category/32-345/',
'https://recipe.rakuten.co.jp/category/32-346/',
'https://recipe.rakuten.co.jp/category/32-347/',
'https://recipe.rakuten.co.jp/category/32-348/',
'https://recipe.rakuten.co.jp/category/32-349/',
'https://recipe.rakuten.co.jp/category/33-350/',
'https://recipe.rakuten.co.jp/category/33-351/',
'https://recipe.rakuten.co.jp/category/33-352/',
'https://recipe.rakuten.co.jp/category/33-353/',
'https://recipe.rakuten.co.jp/category/33-354/',
'https://recipe.rakuten.co.jp/category/33-355/',
'https://recipe.rakuten.co.jp/category/33-356/',
'https://recipe.rakuten.co.jp/category/33-357/',
'https://recipe.rakuten.co.jp/category/33-358/',
'https://recipe.rakuten.co.jp/category/33-359/',
'https://recipe.rakuten.co.jp/category/33-360/',
'https://recipe.rakuten.co.jp/category/33-361/',
'https://recipe.rakuten.co.jp/category/33-362/',
'https://recipe.rakuten.co.jp/category/33-363/',
'https://recipe.rakuten.co.jp/category/33-364/',
'https://recipe.rakuten.co.jp/category/33-365/',
'https://recipe.rakuten.co.jp/category/33-366/',
'https://recipe.rakuten.co.jp/category/33-367/',
'https://recipe.rakuten.co.jp/category/33-721/',
'https://recipe.rakuten.co.jp/category/14-121/',
'https://recipe.rakuten.co.jp/category/14-131/',
'https://recipe.rakuten.co.jp/category/14-126/',
'https://recipe.rakuten.co.jp/category/14-124/',
'https://recipe.rakuten.co.jp/category/14-122/',
'https://recipe.rakuten.co.jp/category/14-123/',
'https://recipe.rakuten.co.jp/category/14-125/',
'https://recipe.rakuten.co.jp/category/14-127/',
'https://recipe.rakuten.co.jp/category/14-368/',
'https://recipe.rakuten.co.jp/category/14-128/',
'https://recipe.rakuten.co.jp/category/14-129/',
'https://recipe.rakuten.co.jp/category/14-130/',
'https://recipe.rakuten.co.jp/category/14-132/',
'https://recipe.rakuten.co.jp/category/14-133/',
'https://recipe.rakuten.co.jp/category/14-134/',
'https://recipe.rakuten.co.jp/category/14-135/',
'https://recipe.rakuten.co.jp/category/14-271/',
'https://recipe.rakuten.co.jp/category/15-687/',
'https://recipe.rakuten.co.jp/category/15-137/',
'https://recipe.rakuten.co.jp/category/15-676/',
'https://recipe.rakuten.co.jp/category/15-681/',
'https://recipe.rakuten.co.jp/category/15-369/',
'https://recipe.rakuten.co.jp/category/15-677/',
'https://recipe.rakuten.co.jp/category/15-683/',
'https://recipe.rakuten.co.jp/category/15-682/',
'https://recipe.rakuten.co.jp/category/15-678/',
'https://recipe.rakuten.co.jp/category/15-679/',
'https://recipe.rakuten.co.jp/category/15-684/',
'https://recipe.rakuten.co.jp/category/15-680/',
'https://recipe.rakuten.co.jp/category/15-138/',
'https://recipe.rakuten.co.jp/category/15-139/',
'https://recipe.rakuten.co.jp/category/15-140/',
'https://recipe.rakuten.co.jp/category/15-141/',
'https://recipe.rakuten.co.jp/category/15-142/',
'https://recipe.rakuten.co.jp/category/15-685/',
'https://recipe.rakuten.co.jp/category/15-686/',
'https://recipe.rakuten.co.jp/category/15-143/',
'https://recipe.rakuten.co.jp/category/15-145/',
'https://recipe.rakuten.co.jp/category/15-146/',
'https://recipe.rakuten.co.jp/category/15-144/',
'https://recipe.rakuten.co.jp/category/15-147/',
'https://recipe.rakuten.co.jp/category/15-151/',
'https://recipe.rakuten.co.jp/category/15-382/',
'https://recipe.rakuten.co.jp/category/16-152/',
'https://recipe.rakuten.co.jp/category/16-153/',
'https://recipe.rakuten.co.jp/category/16-154/',
'https://recipe.rakuten.co.jp/category/16-155/',
'https://recipe.rakuten.co.jp/category/16-156/',
'https://recipe.rakuten.co.jp/category/16-383/',
'https://recipe.rakuten.co.jp/category/16-384/',
'https://recipe.rakuten.co.jp/category/16-272/',
'https://recipe.rakuten.co.jp/category/16-385/',
'https://recipe.rakuten.co.jp/category/16-386/',
'https://recipe.rakuten.co.jp/category/16-158/',
'https://recipe.rakuten.co.jp/category/17-159/',
'https://recipe.rakuten.co.jp/category/17-161/',
'https://recipe.rakuten.co.jp/category/17-387/',
'https://recipe.rakuten.co.jp/category/17-160/',
'https://recipe.rakuten.co.jp/category/17-388/',
'https://recipe.rakuten.co.jp/category/17-169/',
'https://recipe.rakuten.co.jp/category/17-389/',
'https://recipe.rakuten.co.jp/category/17-171/',
'https://recipe.rakuten.co.jp/category/17-168/',
'https://recipe.rakuten.co.jp/category/17-167/',
'https://recipe.rakuten.co.jp/category/17-170/',
'https://recipe.rakuten.co.jp/category/17-164/',
'https://recipe.rakuten.co.jp/category/17-165/',
'https://recipe.rakuten.co.jp/category/17-166/',
'https://recipe.rakuten.co.jp/category/17-173/',
'https://recipe.rakuten.co.jp/category/17-390/',
'https://recipe.rakuten.co.jp/category/17-162/',
'https://recipe.rakuten.co.jp/category/23-392/',
'https://recipe.rakuten.co.jp/category/23-394/',
'https://recipe.rakuten.co.jp/category/23-391/',
'https://recipe.rakuten.co.jp/category/23-399/',
'https://recipe.rakuten.co.jp/category/23-395/',
'https://recipe.rakuten.co.jp/category/23-401/',
'https://recipe.rakuten.co.jp/category/23-404/',
'https://recipe.rakuten.co.jp/category/23-397/',
'https://recipe.rakuten.co.jp/category/23-393/',
'https://recipe.rakuten.co.jp/category/23-403/',
'https://recipe.rakuten.co.jp/category/23-400/',
'https://recipe.rakuten.co.jp/category/23-396/',
'https://recipe.rakuten.co.jp/category/23-405/',
'https://recipe.rakuten.co.jp/category/23-407/',
'https://recipe.rakuten.co.jp/category/23-412/',
'https://recipe.rakuten.co.jp/category/23-406/',
'https://recipe.rakuten.co.jp/category/23-398/',
'https://recipe.rakuten.co.jp/category/23-413/',
'https://recipe.rakuten.co.jp/category/23-411/',
'https://recipe.rakuten.co.jp/category/23-409/',
'https://recipe.rakuten.co.jp/category/23-410/',
'https://recipe.rakuten.co.jp/category/23-402/',
'https://recipe.rakuten.co.jp/category/23-698/',
'https://recipe.rakuten.co.jp/category/23-723/',
'https://recipe.rakuten.co.jp/category/23-408/',
'https://recipe.rakuten.co.jp/category/23-234/',
'https://recipe.rakuten.co.jp/category/18-415/',
'https://recipe.rakuten.co.jp/category/18-424/',
'https://recipe.rakuten.co.jp/category/18-421/',
'https://recipe.rakuten.co.jp/category/18-189/',
'https://recipe.rakuten.co.jp/category/18-187/',
'https://recipe.rakuten.co.jp/category/18-417/',
'https://recipe.rakuten.co.jp/category/18-416/',
'https://recipe.rakuten.co.jp/category/18-418/',
'https://recipe.rakuten.co.jp/category/18-722/',
'https://recipe.rakuten.co.jp/category/18-419/',
'https://recipe.rakuten.co.jp/category/18-420/',
'https://recipe.rakuten.co.jp/category/18-423/',
'https://recipe.rakuten.co.jp/category/18-190/',
'https://recipe.rakuten.co.jp/category/18-703/',
'https://recipe.rakuten.co.jp/category/18-184/',
'https://recipe.rakuten.co.jp/category/18-188/',
'https://recipe.rakuten.co.jp/category/18-185/',
'https://recipe.rakuten.co.jp/category/18-186/',
'https://recipe.rakuten.co.jp/category/18-191/',
'https://recipe.rakuten.co.jp/category/22-432/',
'https://recipe.rakuten.co.jp/category/22-433/',
'https://recipe.rakuten.co.jp/category/22-434/',
'https://recipe.rakuten.co.jp/category/22-435/',
'https://recipe.rakuten.co.jp/category/22-436/',
'https://recipe.rakuten.co.jp/category/22-229/',
'https://recipe.rakuten.co.jp/category/22-221/',
'https://recipe.rakuten.co.jp/category/22-220/',
'https://recipe.rakuten.co.jp/category/22-222/',
'https://recipe.rakuten.co.jp/category/22-219/',
'https://recipe.rakuten.co.jp/category/22-223/',
'https://recipe.rakuten.co.jp/category/22-227/',
'https://recipe.rakuten.co.jp/category/22-231/',
'https://recipe.rakuten.co.jp/category/22-437/',
'https://recipe.rakuten.co.jp/category/22-230/',
'https://recipe.rakuten.co.jp/category/21-204/',
'https://recipe.rakuten.co.jp/category/21-440/',
'https://recipe.rakuten.co.jp/category/21-205/',
'https://recipe.rakuten.co.jp/category/21-438/',
'https://recipe.rakuten.co.jp/category/21-439/',
'https://recipe.rakuten.co.jp/category/21-206/',
'https://recipe.rakuten.co.jp/category/21-215/',
'https://recipe.rakuten.co.jp/category/21-207/',
'https://recipe.rakuten.co.jp/category/21-208/',
'https://recipe.rakuten.co.jp/category/21-209/',
'https://recipe.rakuten.co.jp/category/21-210/',
'https://recipe.rakuten.co.jp/category/21-211/',
'https://recipe.rakuten.co.jp/category/21-216/', 'https://recipe.rakuten.co.jp/category/21-212/', 'https://recipe.rakuten.co.jp/category/21-441/', 'https://recipe.rakuten.co.jp/category/21-442/', 'https://recipe.rakuten.co.jp/category/21-214/', 'https://recipe.rakuten.co.jp/category/21-217/', 'https://recipe.rakuten.co.jp/category/21-218/', 'https://recipe.rakuten.co.jp/category/10-275/', 'https://recipe.rakuten.co.jp/category/10-276/', 'https://recipe.rakuten.co.jp/category/10-277/', 'https://recipe.rakuten.co.jp/category/10-278/', 'https://recipe.rakuten.co.jp/category/10-68/', 'https://recipe.rakuten.co.jp/category/10-66/', 'https://recipe.rakuten.co.jp/category/10-67/', 'https://recipe.rakuten.co.jp/category/10-69/', 'https://recipe.rakuten.co.jp/category/11-70/', 'https://recipe.rakuten.co.jp/category/11-71/', 'https://recipe.rakuten.co.jp/category/11-72/', 'https://recipe.rakuten.co.jp/category/11-73/', 'https://recipe.rakuten.co.jp/category/11-74/', 'https://recipe.rakuten.co.jp/category/11-75/', 'https://recipe.rakuten.co.jp/category/11-76/', 'https://recipe.rakuten.co.jp/category/11-77/', 'https://recipe.rakuten.co.jp/category/11-443/', 'https://recipe.rakuten.co.jp/category/11-78/', 'https://recipe.rakuten.co.jp/category/11-80/', 'https://recipe.rakuten.co.jp/category/11-81/', 'https://recipe.rakuten.co.jp/category/11-79/', 'https://recipe.rakuten.co.jp/category/11-83/', 'https://recipe.rakuten.co.jp/category/11-444/', 'https://recipe.rakuten.co.jp/category/11-82/', 'https://recipe.rakuten.co.jp/category/11-445/', 'https://recipe.rakuten.co.jp/category/11-446/', 'https://recipe.rakuten.co.jp/category/12-447/', 'https://recipe.rakuten.co.jp/category/12-448/', 'https://recipe.rakuten.co.jp/category/12-449/', 'https://recipe.rakuten.co.jp/category/12-450/', 'https://recipe.rakuten.co.jp/category/12-97/', 'https://recipe.rakuten.co.jp/category/12-452/', 'https://recipe.rakuten.co.jp/category/12-98/', 'https://recipe.rakuten.co.jp/category/12-453/', 'https://recipe.rakuten.co.jp/category/12-454/', 'https://recipe.rakuten.co.jp/category/12-99/', 'https://recipe.rakuten.co.jp/category/12-456/', 'https://recipe.rakuten.co.jp/category/12-457/', 'https://recipe.rakuten.co.jp/category/12-455/', 'https://recipe.rakuten.co.jp/category/12-451/', 'https://recipe.rakuten.co.jp/category/12-96/', 'https://recipe.rakuten.co.jp/category/12-458/', 'https://recipe.rakuten.co.jp/category/12-95/', 'https://recipe.rakuten.co.jp/category/12-100/', 'https://recipe.rakuten.co.jp/category/12-101/', 'https://recipe.rakuten.co.jp/category/12-102/', 'https://recipe.rakuten.co.jp/category/12-103/', 'https://recipe.rakuten.co.jp/category/12-105/', 'https://recipe.rakuten.co.jp/category/12-107/', 'https://recipe.rakuten.co.jp/category/12-104/', 'https://recipe.rakuten.co.jp/category/34-688/', 'https://recipe.rakuten.co.jp/category/34-459/', 'https://recipe.rakuten.co.jp/category/34-460/', 'https://recipe.rakuten.co.jp/category/34-461/', 'https://recipe.rakuten.co.jp/category/34-697/', 'https://recipe.rakuten.co.jp/category/34-462/', 'https://recipe.rakuten.co.jp/category/34-690/', 'https://recipe.rakuten.co.jp/category/34-691/', 'https://recipe.rakuten.co.jp/category/34-702/', 'https://recipe.rakuten.co.jp/category/34-692/', 'https://recipe.rakuten.co.jp/category/34-693/', 'https://recipe.rakuten.co.jp/category/34-689/', 'https://recipe.rakuten.co.jp/category/34-695/', 'https://recipe.rakuten.co.jp/category/34-696/', 'https://recipe.rakuten.co.jp/category/19-192/', 'https://recipe.rakuten.co.jp/category/19-193/', 'https://recipe.rakuten.co.jp/category/19-194/', 'https://recipe.rakuten.co.jp/category/19-195/', 'https://recipe.rakuten.co.jp/category/19-196/', 'https://recipe.rakuten.co.jp/category/19-675/', 'https://recipe.rakuten.co.jp/category/19-274/', 'https://recipe.rakuten.co.jp/category/19-463/', 'https://recipe.rakuten.co.jp/category/19-464/', 'https://recipe.rakuten.co.jp/category/19-700/', 'https://recipe.rakuten.co.jp/category/19-710/', 'https://recipe.rakuten.co.jp/category/19-711/', 'https://recipe.rakuten.co.jp/category/19-273/', 'https://recipe.rakuten.co.jp/category/27-266/', 'https://recipe.rakuten.co.jp/category/27-267/', 'https://recipe.rakuten.co.jp/category/27-268/', 'https://recipe.rakuten.co.jp/category/27-465/', 'https://recipe.rakuten.co.jp/category/27-269/', 'https://recipe.rakuten.co.jp/category/35-466/', 'https://recipe.rakuten.co.jp/category/35-467/', 'https://recipe.rakuten.co.jp/category/35-468/', 'https://recipe.rakuten.co.jp/category/35-469/', 'https://recipe.rakuten.co.jp/category/35-470/', 'https://recipe.rakuten.co.jp/category/35-471/', 'https://recipe.rakuten.co.jp/category/35-472/', 'https://recipe.rakuten.co.jp/category/35-473/', 'https://recipe.rakuten.co.jp/category/35-474/', 'https://recipe.rakuten.co.jp/category/35-475/', 'https://recipe.rakuten.co.jp/category/35-476/', 'https://recipe.rakuten.co.jp/category/35-477/', 'https://recipe.rakuten.co.jp/category/13-478/', 'https://recipe.rakuten.co.jp/category/13-706/', 'https://recipe.rakuten.co.jp/category/13-479/', 'https://recipe.rakuten.co.jp/category/13-480/', 'https://recipe.rakuten.co.jp/category/13-481/', 'https://recipe.rakuten.co.jp/category/13-108/', 'https://recipe.rakuten.co.jp/category/13-109/', 'https://recipe.rakuten.co.jp/category/13-482/', 'https://recipe.rakuten.co.jp/category/13-483/', 'https://recipe.rakuten.co.jp/category/13-111/', 'https://recipe.rakuten.co.jp/category/13-112/', 'https://recipe.rakuten.co.jp/category/13-113/', 'https://recipe.rakuten.co.jp/category/13-114/', 'https://recipe.rakuten.co.jp/category/13-484/', 'https://recipe.rakuten.co.jp/category/13-115/', 'https://recipe.rakuten.co.jp/category/20-485/', 'https://recipe.rakuten.co.jp/category/20-197/', 'https://recipe.rakuten.co.jp/category/20-486/', 'https://recipe.rakuten.co.jp/category/20-487/', 'https://recipe.rakuten.co.jp/category/20-488/', 'https://recipe.rakuten.co.jp/category/20-198/', 'https://recipe.rakuten.co.jp/category/20-199/', 'https://recipe.rakuten.co.jp/category/20-200/', 'https://recipe.rakuten.co.jp/category/20-201/', 'https://recipe.rakuten.co.jp/category/20-202/', 'https://recipe.rakuten.co.jp/category/20-203/', 'https://recipe.rakuten.co.jp/category/20-258/', 'https://recipe.rakuten.co.jp/category/36-489/', 'https://recipe.rakuten.co.jp/category/36-490/', 'https://recipe.rakuten.co.jp/category/36-491/', 'https://recipe.rakuten.co.jp/category/36-492/', 'https://recipe.rakuten.co.jp/category/36-493/', 'https://recipe.rakuten.co.jp/category/36-494/', 'https://recipe.rakuten.co.jp/category/36-495/', 'https://recipe.rakuten.co.jp/category/36-496/', 'https://recipe.rakuten.co.jp/category/36-497/', 'https://recipe.rakuten.co.jp/category/36-708/', 'https://recipe.rakuten.co.jp/category/37-498/', 'https://recipe.rakuten.co.jp/category/37-499/', 'https://recipe.rakuten.co.jp/category/37-500/', 'https://recipe.rakuten.co.jp/category/38-501/', 'https://recipe.rakuten.co.jp/category/38-502/', 'https://recipe.rakuten.co.jp/category/38-503/', 'https://recipe.rakuten.co.jp/category/39-504/', 'https://recipe.rakuten.co.jp/category/39-505/', 'https://recipe.rakuten.co.jp/category/39-705/', 'https://recipe.rakuten.co.jp/category/39-699/', 'https://recipe.rakuten.co.jp/category/39-506/', 'https://recipe.rakuten.co.jp/category/39-507/', 'https://recipe.rakuten.co.jp/category/39-508/', 'https://recipe.rakuten.co.jp/category/39-509/', 'https://recipe.rakuten.co.jp/category/39-510/', 'https://recipe.rakuten.co.jp/category/39-511/', 'https://recipe.rakuten.co.jp/category/39-709/', 'https://recipe.rakuten.co.jp/category/39-724/', 'https://recipe.rakuten.co.jp/category/40-512/', 'https://recipe.rakuten.co.jp/category/40-513/', 'https://recipe.rakuten.co.jp/category/40-514/', 'https://recipe.rakuten.co.jp/category/40-707/', 'https://recipe.rakuten.co.jp/category/40-515/', 'https://recipe.rakuten.co.jp/category/40-516/', 'https://recipe.rakuten.co.jp/category/40-704/', 'https://recipe.rakuten.co.jp/category/40-517/', 'https://recipe.rakuten.co.jp/category/40-518/', 'https://recipe.rakuten.co.jp/category/40-519/', 'https://recipe.rakuten.co.jp/category/40-520/', 'https://recipe.rakuten.co.jp/category/40-521/', 'https://recipe.rakuten.co.jp/category/40-522/', 'https://recipe.rakuten.co.jp/category/40-523/', 'https://recipe.rakuten.co.jp/category/40-524/', 'https://recipe.rakuten.co.jp/category/40-525/', 'https://recipe.rakuten.co.jp/category/40-526/', 'https://recipe.rakuten.co.jp/category/40-712/', 'https://recipe.rakuten.co.jp/category/26-262/', 'https://recipe.rakuten.co.jp/category/26-260/', 'https://recipe.rakuten.co.jp/category/26-261/', 'https://recipe.rakuten.co.jp/category/26-265/', 'https://recipe.rakuten.co.jp/category/41-531/', 'https://recipe.rakuten.co.jp/category/41-532/', 'https://recipe.rakuten.co.jp/category/41-533/', 'https://recipe.rakuten.co.jp/category/41-534/', 'https://recipe.rakuten.co.jp/category/41-535/', 'https://recipe.rakuten.co.jp/category/41-536/', 'https://recipe.rakuten.co.jp/category/41-537/', 'https://recipe.rakuten.co.jp/category/41-539/', 'https://recipe.rakuten.co.jp/category/41-542/', 'https://recipe.rakuten.co.jp/category/41-713/', 'https://recipe.rakuten.co.jp/category/41-543/', 'https://recipe.rakuten.co.jp/category/41-538/', 'https://recipe.rakuten.co.jp/category/41-541/', 'https://recipe.rakuten.co.jp/category/41-546/', 'https://recipe.rakuten.co.jp/category/41-547/', 'https://recipe.rakuten.co.jp/category/41-548/', 'https://recipe.rakuten.co.jp/category/41-540/', 'https://recipe.rakuten.co.jp/category/41-544/', 'https://recipe.rakuten.co.jp/category/41-545/', 'https://recipe.rakuten.co.jp/category/41-549/', 'https://recipe.rakuten.co.jp/category/42-550/', 'https://recipe.rakuten.co.jp/category/42-551/', 'https://recipe.rakuten.co.jp/category/42-552/', 'https://recipe.rakuten.co.jp/category/42-553/', 'https://recipe.rakuten.co.jp/category/42-554/', 'https://recipe.rakuten.co.jp/category/42-555/', 'https://recipe.rakuten.co.jp/category/42-565/', 'https://recipe.rakuten.co.jp/category/42-556/', 'https://recipe.rakuten.co.jp/category/42-557/', 'https://recipe.rakuten.co.jp/category/42-558/', 'https://recipe.rakuten.co.jp/category/42-559/', 'https://recipe.rakuten.co.jp/category/42-560/', 'https://recipe.rakuten.co.jp/category/42-561/', 'https://recipe.rakuten.co.jp/category/42-714/', 'https://recipe.rakuten.co.jp/category/42-562/', 'https://recipe.rakuten.co.jp/category/42-563/', 'https://recipe.rakuten.co.jp/category/42-564/', 'https://recipe.rakuten.co.jp/category/42-566/', 'https://recipe.rakuten.co.jp/category/42-567/', 'https://recipe.rakuten.co.jp/category/42-568/', 'https://recipe.rakuten.co.jp/category/43-569/', 'https://recipe.rakuten.co.jp/category/43-570/', 'https://recipe.rakuten.co.jp/category/43-578/', 'https://recipe.rakuten.co.jp/category/43-571/', 'https://recipe.rakuten.co.jp/category/43-577/', 'https://recipe.rakuten.co.jp/category/43-572/', 'https://recipe.rakuten.co.jp/category/43-573/', 'https://recipe.rakuten.co.jp/category/43-574/', 'https://recipe.rakuten.co.jp/category/43-575/', 'https://recipe.rakuten.co.jp/category/43-576/', 'https://recipe.rakuten.co.jp/category/43-579/', 'https://recipe.rakuten.co.jp/category/43-580/', 'https://recipe.rakuten.co.jp/category/43-581/', 'https://recipe.rakuten.co.jp/category/43-582/', 'https://recipe.rakuten.co.jp/category/44-583/', 'https://recipe.rakuten.co.jp/category/44-584/', 'https://recipe.rakuten.co.jp/category/44-585/', 'https://recipe.rakuten.co.jp/category/44-586/', 'https://recipe.rakuten.co.jp/category/44-587/', 'https://recipe.rakuten.co.jp/category/44-588/', 'https://recipe.rakuten.co.jp/category/44-589/', 'https://recipe.rakuten.co.jp/category/44-590/', 'https://recipe.rakuten.co.jp/category/44-591/', 'https://recipe.rakuten.co.jp/category/25-256/', 'https://recipe.rakuten.co.jp/category/25-701/', 'https://recipe.rakuten.co.jp/category/25-248/', 'https://recipe.rakuten.co.jp/category/25-255/', 'https://recipe.rakuten.co.jp/category/25-257/', 'https://recipe.rakuten.co.jp/category/46-596/', 'https://recipe.rakuten.co.jp/category/46-597/', 'https://recipe.rakuten.co.jp/category/46-598/', 'https://recipe.rakuten.co.jp/category/46-599/', 'https://recipe.rakuten.co.jp/category/47-602/', 'https://recipe.rakuten.co.jp/category/47-600/', 'https://recipe.rakuten.co.jp/category/47-601/', 'https://recipe.rakuten.co.jp/category/47-603/', 'https://recipe.rakuten.co.jp/category/47-604/', 'https://recipe.rakuten.co.jp/category/47-605/', 'https://recipe.rakuten.co.jp/category/47-606/', 'https://recipe.rakuten.co.jp/category/47-607/', 'https://recipe.rakuten.co.jp/category/47-608/', 'https://recipe.rakuten.co.jp/category/47-609/', 'https://recipe.rakuten.co.jp/category/47-610/', 'https://recipe.rakuten.co.jp/category/48-612/', 'https://recipe.rakuten.co.jp/category/48-613/', 'https://recipe.rakuten.co.jp/category/48-611/', 'https://recipe.rakuten.co.jp/category/48-614/', 'https://recipe.rakuten.co.jp/category/48-615/', 'https://recipe.rakuten.co.jp/category/48-616/', 'https://recipe.rakuten.co.jp/category/48-617/', 'https://recipe.rakuten.co.jp/category/48-618/', 'https://recipe.rakuten.co.jp/category/48-619/', 'https://recipe.rakuten.co.jp/category/48-620/', 'https://recipe.rakuten.co.jp/category/48-621/', 'https://recipe.rakuten.co.jp/category/48-622/', 'https://recipe.rakuten.co.jp/category/48-623/', 'https://recipe.rakuten.co.jp/category/48-624/', 'https://recipe.rakuten.co.jp/category/48-625/', 'https://recipe.rakuten.co.jp/category/48-626/', 'https://recipe.rakuten.co.jp/category/48-627/', 'https://recipe.rakuten.co.jp/category/48-628/', 'https://recipe.rakuten.co.jp/category/48-629/', 'https://recipe.rakuten.co.jp/category/48-715/', 'https://recipe.rakuten.co.jp/category/48-716/', 'https://recipe.rakuten.co.jp/category/48-630/', 'https://recipe.rakuten.co.jp/category/24-631/', 'https://recipe.rakuten.co.jp/category/24-632/', 'https://recipe.rakuten.co.jp/category/24-633/', 'https://recipe.rakuten.co.jp/category/24-634/', 'https://recipe.rakuten.co.jp/category/24-635/', 'https://recipe.rakuten.co.jp/category/24-238/', 'https://recipe.rakuten.co.jp/category/24-244/', 'https://recipe.rakuten.co.jp/category/49-636/', 'https://recipe.rakuten.co.jp/category/49-637/', 'https://recipe.rakuten.co.jp/category/49-638/', 'https://recipe.rakuten.co.jp/category/49-639/', 'https://recipe.rakuten.co.jp/category/49-640/', 'https://recipe.rakuten.co.jp/category/49-641/', 'https://recipe.rakuten.co.jp/category/49-642/', 'https://recipe.rakuten.co.jp/category/49-643/', 'https://recipe.rakuten.co.jp/category/49-644/', 'https://recipe.rakuten.co.jp/category/49-645/', 'https://recipe.rakuten.co.jp/category/49-646/', 'https://recipe.rakuten.co.jp/category/49-648/', 'https://recipe.rakuten.co.jp/category/49-649/', 'https://recipe.rakuten.co.jp/category/49-650/', 'https://recipe.rakuten.co.jp/category/49-651/', 'https://recipe.rakuten.co.jp/category/50-652/', 'https://recipe.rakuten.co.jp/category/50-653/', 'https://recipe.rakuten.co.jp/category/50-654/', 'https://recipe.rakuten.co.jp/category/50-655/', 'https://recipe.rakuten.co.jp/category/50-656/', 'https://recipe.rakuten.co.jp/category/51-657/', 'https://recipe.rakuten.co.jp/category/51-658/', 'https://recipe.rakuten.co.jp/category/51-659/', 'https://recipe.rakuten.co.jp/category/52-660/', 'https://recipe.rakuten.co.jp/category/52-661/', 'https://recipe.rakuten.co.jp/category/52-662/', 'https://recipe.rakuten.co.jp/category/52-663/', 'https://recipe.rakuten.co.jp/category/53-664/', 'https://recipe.rakuten.co.jp/category/53-665/', 'https://recipe.rakuten.co.jp/category/53-666/', 'https://recipe.rakuten.co.jp/category/53-667/', 'https://recipe.rakuten.co.jp/category/54-668/', 'https://recipe.rakuten.co.jp/category/54-669/', 'https://recipe.rakuten.co.jp/category/54-670/', 'https://recipe.rakuten.co.jp/category/55-671/', 'https://recipe.rakuten.co.jp/category/55-672/', 'https://recipe.rakuten.co.jp/category/55-673/', 'https://recipe.rakuten.co.jp/category/55-674/'
"""