# Project Note : components

필요한 UI 컴포넌트들을 직접 구현하였는데, 다른 프로젝트에서도 추후에 사용되면 좋을 것 같아서 기록한다. 

하나하나 모으다보면 언젠가 나도 [Vuexy](https://pixinvent.com/demo/vuexy-react-admin-dashboard-template/demo-4/dashboard/ecommerce) 와 같은 컴포넌트 Set 을 개발할 수 있지 않을까..? 



아래는 모두 vanilla CSS + tailwind CSS 를 활용했다. 

## Tab

탭으로 활용 가능한 컴포넌트

`TabBar.jsx`

```react
import { useEffect, useRef } from "react";
import TabItem from "./TabItem";
import "./TabBar.css";

export default function TabBar({
  currentTab,
  setCurrentTab,
  tabInfo,
  baseURL,
}) {
  const marker = useRef();

  useEffect(() => {
    let selectedTab;
    if (currentTab) {
      selectedTab = document.querySelectorAll(".tab-item");
      for (let i = 0; i < selectedTab.length; i++) {
        if (selectedTab[i].innerText === currentTab) {
          selectedTab = selectedTab[i];
          break;
        }
      }
    } else {
      selectedTab = document.querySelector(".tab-item");
    }
    marker.current.style.left = selectedTab.offsetLeft + "px";
    marker.current.style.width = selectedTab.offsetWidth + "px";
  }, [currentTab]);

  const indicator = (e) => {
    marker.current.style.left = e.offsetLeft + "px";
    marker.current.style.width = e.offsetWidth + "px";
  };

  const handleOnClick = (e, text) => {
    indicator(e.target);
    setCurrentTab(text);
  };

  const setting = {
    종합정보: "detail",
    뉴스: "news",
    "종목토론 게시판": "board",
  };

  const paintTabItem = tabInfo.map((text, index) => (
    <TabItem
      key={index}
      handleOnClick={handleOnClick}
      text={text}
      link={setting[text] ? baseURL + `/${setting[text]}` : ""}
    />
  ));

  return (
    <div className="tab-box h-10 w-max border-b-4">
      <div ref={marker} className="marker"></div>
      {paintTabItem}
    </div>
  );
}
```



`TabItem.jsx`

```react
import { Link } from "react-router-dom";

export default function TabItem({ link, text, handleOnClick }) {
  return (
    <Link
      to={link}
      onClick={(e) => handleOnClick(e, text)}
      className="tab-item"
    >
      {text}
    </Link>
  );
}
```



`TabBar.css`

```css
.tab-box {
  position: relative;
  display: flex;
}

.tab-item {
  position: relative;
  padding: 0 20px;
}

.tab-box .marker {
  position: absolute;
  left: 0;
  width: 0;
  height: 4px;
  bottom: -4px;
  transition: 0.5s;
  border-radius: 4px;
  background: #18216d;
}
```



아래와 같이 활용할 수 있다. 

```react
export default function MyPage() {
  // tab 이동 시 시용
  const [currentTab, setCurrentTab] = useState("관심종목");
  const tabInfo = ["관심종목", "포트폴리오", "회원정보 수정"];

  return (
    <PageContainer>
      <div className="flex flex-col items-center">
        <TabBar setCurrentTab={setCurrentTab} tabInfo={tabInfo} />
        <div className="mt-5 w-full">
          {currentTab === "관심종목" && <InterestingStock />}
          {currentTab === "포트폴리오" && <Portfolio />}
          {currentTab === "회원정보 수정" && <UserUpdate />}
        </div>
      </div>
    </PageContainer>
  );
}
```

- `<TabBar/>` 에서 `onClick` 이벤트에 의해 `currentTab` state 값이 변경될 때마다 각각 다른 컴포넌트를 렌더링한다. 



## Sidebar 

좌측에 위치하여 hover 하였을 때 확장되는 사이드바 컴포넌트 

`SideBar.jsx`

```react
import { Link, useLocation } from "react-router-dom";
import NavItem from "./NavItem";
import { ReactComponent as DashboardIconActive } from "../../assets/dashboardIconActive.svg";
import { ReactComponent as StockList } from "../../assets/stockList.svg";
// ... 

export default function SideBar() {
  const location = useLocation();
  const currentPath = location.pathname;
  const linkInfo = [
    {
      icon: <DashboardIconActive />,
      linkPath: "/market",
      linkText: "주요 시세 정보",
    },
    {
      icon: <StockList />,
      linkPath: "/stock",
      linkText: "종목 리스트",
    },
    // ... 
  ];

  const paintNavItems = linkInfo.map((info, index) => (
    <NavItem
      key={index}
      currentPath={currentPath}
      linkPath={info.linkPath}
      linkText={info.linkText}
    >
      {info.icon}
    </NavItem>
  ));

  return (
    <div className="navbar h-screen bg-white flex flex-col items-center pt-10 drop-shadow">
      <ul className="w-full mt-10 flex flex-col">
        <li className="logo">
          <Link to="/" className="flex items-center">
            <span className="link-text">JRstock</span>
            <Rocket />
          </Link>
        </li>
        {paintNavItems}
      </ul>
    </div>
  );
}
```



`NavItem.jsx`

```react
import { Link } from "react-router-dom";

export default function NavItem({ currentPath, linkPath, linkText, children }) {
  const active = "nav-link";
  const inActive =
    "nav-link grayscale opacity-50 hover:grayscale-0 hover:opacity-100";

  return (
    <li className="nav-item hover:bg-indigo-50">
      <Link to={linkPath}>
        <div className={currentPath.includes(linkPath) ? active : inActive}>
          {children}
          <span className="link-text">{linkText}</span>
        </div>
      </Link>
    </li>
  );
}
```



`SideBar.css`

```css
.link-text {
  display: none;
  margin-left: 0.5rem;
  color: #18216d;
}

.navbar {
  width: 5rem;
  height: 100vh;
  position: fixed;
  transition: width 200ms ease;
  z-index: 40;
}

.logo {
  font-size: 1.7rem;
  font-weight: bold;
  text-align: center;
  letter-spacing: 0.3ch;
  margin-bottom: 3rem;
  display: flex;
  align-items: center;
  height: 5rem;
  text-decoration: none;
  transition: all 200ms ease;
  padding-left: 1.5rem;
}

.logo svg {
  transform: rotate(0deg);
  transition: all 500ms ease;
}

.navbar:hover .logo svg {
  transform: rotate(-180deg);
  fill: #ff825c;
}

.navbar:hover {
  width: 16rem;
}

.navbar:hover .link-text {
  display: block;
  white-space: nowrap;
}

.nav-item {
  width: 100%;
}

.nav-item:last-child {
  margin-top: auto;
}

.nav-link {
  display: flex;
  align-items: center;
  height: 5rem;
  text-decoration: none;
  transition: all 200ms ease;
  padding-left: 1.5rem;
}

.nav-link svg {
  min-width: 2rem;
}
```

