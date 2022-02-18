import React from "react";
import { render } from "react-dom";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Link,
  RouteComponentProps,
  RouteProps
} from 'react-router-dom';

import SuperAdminDashboard from "./pages/superAdmin/SuperAdminDashboard"
import SuperAdminMenuMain from "./pages/superAdmin/SuperAdminMenuMain";

import Dashboard from "./pages/common/Dashboard";
import TaskList from "./pages/common/TaskList";
import ManualTaskList from "./pages/common/manualTask/ManualTaskList";
import AdminClientAction from "./pages/admin/AdminClientAction";
import AdminEmpAction from "./pages/admin/AdminEmpAction";
import AdminInsight from "./pages/admin/AdminInsight";
import NotificationTable from "./pages/common/NotificationTable";
import Calendar from "./pages/common/Calendar"
import AdminSettings from "./pages/admin/AdminSettings";
import ContactUs from "./pages/common/ContactUs";
import LeadTracking from "./pages/common/LeadTracking";

import ClientDashboardLanding from "./pages/common/clientDashboard/ClientDashboardLanding";
import ClientDashboard, { IClientDashboardProps } from "./pages/common/clientDashboard/Dashboard/ClientDashboard";
import ClientCommunication from "./pages/common/clientDashboard/ClientCommunication";
import ClientDocument from "./pages/common/clientDashboard/ClientDocument";
import ClientStatus from "./pages/common/clientDashboard/ClientStatus";
import ClientBusiness from "./pages/common/clientDashboard/ClientBusiness";
import ClientOrganizer from "./pages/common/clientDashboard/ClientOrganizer";
import ClientInvoice from "./pages/common/clientDashboard/ClientInvoice";
import ClientProject from "./pages/common/clientDashboard/ClientProject";
import ClientDependent from "./pages/common/clientDashboard/ClientDependent";
import ClientList from "./pages/recep/ClientList";
import Footer from "./pages/common/Footer";

import AdminMenuMain from "./pages/common/AdminMenuMain";
import Splashscreen from "../intelws_portal/constructs/elements/Splashscreen";
import * as urls from './Urls';

import { get, getCancelToken } from "../intelws_portal/utils/backendInterface";
import { IDataRepr } from "../intelws_portal/constructs/elements/Table";
import { ITabRepr } from "../intelws_portal/constructs/elements/Tabs";
import { AxiosResponse } from "axios";
import Tickets from "./pages/admin/tickets/TicketsMainPage";
import TicketsDetails from "./pages/admin/tickets/TicketsDetails";
import ManualTaskDetailsDashboard from "./pages/common/manualTask/ManualTaskDetailsDashboard";
import ManualTaskDashboardLanding from "./pages/common/manualTask/ManualTaskDashboardLanding";
import PayInvoice from "./pages/client/PayInvoice";
import SuperAdminLeads from "./pages/superAdmin/SuperAdminLeads";
import AdminSignup from "./pages/common/external_links/authentication/AdminSignup";
import Signin from "./pages/common/external_links/authentication/Signin";
import ClientSignup from "./pages/common/external_links/authentication/ClientSignup";
import ClientActivation from "./pages/common/external_links/authentication/ClientActivation";
import ResetPassword from "./pages/common/external_links/authentication/ResetPassword";
import ChangePassword from "./pages/common/external_links/authentication/ChangePassword";
import ForgotPassword from "./pages/common/external_links/authentication/ForgotPassword";
import AdminHomePage from "./pages/common/external_links/admin_home_pages/AdminHomePage";
import AdminAboutUs from "./pages/common/external_links/admin_home_pages/AdminAboutUs";
import AdminServicesPage from "./pages/common/external_links/admin_home_pages/AdminServicesPage";
import Logout from "./pages/common/external_links/authentication/Logout";
import ReferralReview from "./pages/common/ReferralReview";
import AdminBulkMsg from "./pages/admin/AdminBulkMsg";

export interface IMenuOptionsConfig {
  /* Common Options */
  is_sa?: boolean,
  is_user?: boolean,
  dashboard?: boolean,
  workflow?: boolean,
  manual_task?: boolean,
  client?: boolean,
  client_actions?: boolean,
  calendar?: boolean,
  settings?: boolean,
  tickets?: boolean,
  initials?: string,
  client_card?: boolean,
  lead_tracking?: boolean,
  password_management?: boolean

  client_dashboard_option?: boolean,
  client_documents_option?: boolean,
  client_status_option?: boolean,
  client_business_option?: boolean,
  client_organizer_option?: boolean,

  team?: boolean,
  insight?: boolean,
  recep_client?: boolean,
  client_dashboard?: ITabRepr[],
  project_dashboard?: ITabRepr[],
  notification_table?: boolean

  client_message?: boolean,
  team_message?: boolean,
  notes?: boolean,
  todo_edit?: boolean,
  business_edit?: boolean,

  show_nav_bar?: boolean,
}

interface IFetchAppConfig extends AxiosResponse {
  data: IMenuOptionsConfig
}

function App() {
  const [isLoaded, setIsLoaded] = React.useState(false);
  const [currentPage, setCurrentPage] = React.useState("");
  const [bnsValues, setBnsValues] = React.useState<number[]>([]);
  const [bnsShow, setBnsShow] = React.useState<string[]>([]);
  const [menuOptionsConfig, setMenuOptionsConfig] = React.useState<(IMenuOptionsConfig)>({});
  const [cpaLogoUrl, setCpaLogoUrl] = React.useState<string>()
  const cancelTokenSource = React.useRef(getCancelToken());

  React.useEffect(() => {
    const configRequestResponse = get(urls.CONFIG_ENDPOINT, cancelTokenSource.current.token) as Promise<IFetchAppConfig>;
    configRequestResponse.then((response) => {
      setMenuOptionsConfig(response.data);
      setIsLoaded(true);
    })
  }, [])


  function bnsDocCallback(bnsData: IDataRepr[]) {
    let bnsShow = ["Select Business"];
    let bnsValues = [0];
    bnsData.forEach((ele) => {
      bnsShow.push(ele.bns_name as string);
      bnsValues.push(ele.id);
    })
    setBnsShow(bnsShow);
    setBnsValues(bnsValues);
  }

  function bnsOperCallback(bns: IDataRepr, oper: string) {
    setBnsValues((prevBnsValues) => {
      return [...prevBnsValues, bns.id];
    })
    setBnsShow((prevBnsShow) => {
      return [...prevBnsShow, bns.bns_name as string];
    })
  }

  function getMenuOptionsConfig() {
    return menuOptionsConfig;
  }

  function setMenuOptionsConfigNoNavBar() {
    setMenuOptionsConfig({ show_nav_bar: false });
  }

  if (!isLoaded) {
    return (
      <Splashscreen />
    )
  } else {
    return (
      <Router>
        <React.Fragment>
          <div className="App">
            <React.Fragment>
              <Switch>
                <Route exact path={urls.ADMIN_SIGNUP}
                  render={(props: any) => <AdminSignup />} />
                <Route exact path={urls.G_SIGNIN}
                  render={(props: any) => <Signin isRegularSignin={true} />} />
                <Route exact path={urls.LOGOUT}
                  render={(props: any) => <Logout />} />
                <Route exact path={urls.ADMIN_HOME}
                  render={(props: any) => <AdminHomePage {...props} />} />
                <Route exact path={urls.ADMIN_ABOUTUS}
                  render={(props: any) => <AdminAboutUs {...props}/>} />
                <Route exact path={urls.ADMIN_SERVICES}
                  render={(props: any) => <AdminServicesPage {...props}/>} />
                <Route exact path={urls.ADMIN_SIGNIN}
                  render={(props: any) => <Signin {...props} />} />
                <Route exact path={urls.CLIENT_SIGNUP}
                  render={(props: any) => <ClientSignup {...props} />} />
                <Route exact path={urls.REFER_CLIENT_SIGNUP}
                  render={(props: any) => <ClientSignup {...props} />} />
                <Route exact path={urls.CLIENT_ACTIVATION}
                  render={(props: any) => <ClientActivation {...props} />} />
                <Route exact path={urls.RESET_PASSWORD}
                  render={(props: any) => <ResetPassword {...props} />} />
                <Route exact path={urls.CHANGE_PASSWORD}
                  render={(props: any) => <ChangePassword {...props} />} />
                <Route exact path={urls.FORGOT_PASSWORD}
                  render={(props: any) => <ForgotPassword isRegularForgotPassword={true} />} />
                <Route exact path={urls.ADMIN_FORGOT_PASSWORD}
                  render={(props: any) => <ForgotPassword {...props} />} />
                <Route exact path={urls.CONTACT_US}
                  render={(props: any) => <ContactUs {...props} />} />
                <Route exact path={urls.REFER_CONTACT_US}
                  render={(props: any) => <ContactUs {...props} />} />
                <Route exact path={urls.PAY_INVOICE}
                  render={(props: any) => <PayInvoice {...props} />} />
                <div className="page-wrapper">
                  <div className="right-body-content-wrapper">
                    {(() => {
                      if (menuOptionsConfig.is_sa && (menuOptionsConfig.show_nav_bar == undefined || (menuOptionsConfig.show_nav_bar != undefined && menuOptionsConfig.show_nav_bar))) {
                        return (
                          <SuperAdminMenuMain {...menuOptionsConfig}
                            currentPage={currentPage} />
                        )
                      } else {
                        if ((menuOptionsConfig.show_nav_bar == undefined || (menuOptionsConfig.show_nav_bar != undefined && menuOptionsConfig.show_nav_bar))) {
                          return (
                            <AdminMenuMain {...menuOptionsConfig}
                              currentPage={currentPage} cpaLogoUrl={cpaLogoUrl} setCpaLogoUrl={setCpaLogoUrl} />
                          )
                        }
                      }
                    })()}
                    <Route exact path={urls.PAY_INVOICE}
                      render={(props: any) => <PayInvoice resetNavBar={setMenuOptionsConfigNoNavBar}
                        {...props} />} />
                    <Route exact path={urls.USER_REFER_REVIEW}
                      render={(props: any) => <ReferralReview mutator={{ currentPage: setCurrentPage }} {...props} />} />
                    <Route exact path={urls.SUPER_ADMIN_DASHBOARD}
                      render={(props) => <SuperAdminDashboard
                        mutator={{ currentPage: setCurrentPage }} {...props} />}>
                    </Route>
                    <Route exact path={urls.SUPER_ADMIN_LEADS}
                      render={(props) => <SuperAdminLeads
                        mutator={{ currentPage: setCurrentPage }} {...props} />}>
                    </Route>

                    <Route exact path={urls.ADMIN_DASHBOARD}
                      render={(props) => <Dashboard mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>

                    <Route exact path={urls.COMMON_TASK_LIST}
                      render={(props) => <TaskList mutator={{ currentPage: setCurrentPage }}
                        {...props} />} >
                    </Route>

                    <Route exact path={urls.COMMON_MANUAL_TASK_LIST}
                      render={(props) => <ManualTaskList mutator={{ currentPage: setCurrentPage }}
                        {...props} />} >
                    </Route>

                    <Route exact path={urls.MANUAL_TASK_DETAILS}
                      render={(props: any) => <ManualTaskDashboardLanding mutator={{ currentPage: setCurrentPage, getMenuOptionsConfig: getMenuOptionsConfig }}
                        {...props} />} >
                    </Route>

                    <Route exact path={urls.ADMIN_CLIENT_ACTION}
                      render={(props) => <AdminClientAction mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>

                    <Route exact path={urls.ADMIN_EMP_ACTION}
                      render={(props) => <AdminEmpAction mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>

                    <Route exact path={urls.ADMIN_INSIGHT}
                      render={(props) => <AdminInsight mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>

                    <Route exact path={urls.ADMIN_BULK_MSG}
                      render={(props) => <AdminBulkMsg 
                      userIds={[]} triggerClose={function (): void {
                        throw new Error("Function not implemented.");
                      } } {...props} />}>
                    </Route>

                    <Route exact path={urls.ADMIN_NOTIFICATIONS}
                      render={(props) => <NotificationTable mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>

                    <Route exact path={urls.ADMIN_SCHEDULER}
                      render={(props) => <Calendar mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>

                    <Route exact path={urls.ADMIN_SETTINGS}
                      render={(props) => <AdminSettings mutator={{ currentPage: setCurrentPage }}
                        {...props} cpaLogoUrl={cpaLogoUrl} setCpaLogoUrl={setCpaLogoUrl} />}>
                    </Route>

                    <Route exact path={urls.TICKETS}
                      render={(props) => <Tickets />} />

                    <Route exact path={urls.TICKETS_DETAILS}
                      render={(props: any) => <TicketsDetails {...props} />} />

                    <Route exact path={urls.LEADS}
                      render={(props) => <LeadTracking {...props}
                        mutator={{ currentPage: setCurrentPage }} />} />

                    <Route path={urls.COMMON_CLIENT_DASHBOARD}
                      render={(props: any) => <ClientDashboardLanding
                        mutator={{ currentPage: setCurrentPage, getMenuOptionsConfig: getMenuOptionsConfig }}
                        {...props} />}>
                    </Route>

                    <Route path={urls.RECEP_CLIENT_LIST}
                      render={(props) => <ClientList mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>
                    <Route path={urls.CLIENT_DASHBOARD}
                      render={(props: any) => <ClientDashboard {...props}
                        mutator={{ currentPage: setCurrentPage, getMenuOptionsConfig: getMenuOptionsConfig }} />}>
                    </Route>

                    <Route path={urls.CLIENT_COMMUNICATION}
                      render={(props: any) => <ClientCommunication mutator={{ currentPage: setCurrentPage, getMenuOptionsConfig: getMenuOptionsConfig }}
                        {...props} />}>
                    </Route>

                    <Route path={urls.CLIENT_DOCUMENT}
                      render={(props: any) => <ClientDocument mutator={{ currentPage: setCurrentPage, bnsDocCallback: bnsDocCallback }}
                        bnsValues={bnsValues} bnsShow={bnsShow} {...props} />}>
                    </Route>

                    <Route path={urls.CLIENT_STATUS}
                      render={(props: any) => <ClientStatus mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>

                    <Route path={urls.CLIENT_BUSINESS}
                      render={(props: any) => <ClientBusiness
                        mutator={{ currentPage: setCurrentPage, bnsOperCallback: bnsOperCallback, getMenuOptionsConfig: getMenuOptionsConfig }}
                        {...props} />}>
                    </Route>

                    <Route path={urls.CLIENT_ORGANIZER}
                      render={(props) => <ClientOrganizer mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>

                    <Route path={urls.CLIENT_INVOICE}
                      render={(props: any) => <ClientInvoice mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>

                    <Route path={urls.CLIENT_PROJECT}
                      render={(props: any) => <ClientProject mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>

                    <Route path={urls.CLIENT_DEPENDENT}
                      render={(props: any) => <ClientDependent mutator={{ currentPage: setCurrentPage }}
                        {...props} />}>
                    </Route>

                  </div>
                </div>
              </Switch>
            </React.Fragment>
            <Footer />
          </div>
        </React.Fragment>
      </Router>
    )
  }
}

export default App;