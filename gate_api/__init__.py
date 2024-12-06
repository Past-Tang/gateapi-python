# coding: utf-8

# flake8: noqa

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "4.86.0"

# import apis into sdk package
from gate_api.api.earn_uni_api import EarnUniApi
from gate_api.api.margin_uni_api import MarginUniApi
from gate_api.api.sub_account_api import SubAccountApi
from gate_api.api.unified_api import UnifiedApi
from gate_api.api.account_api import AccountApi
from gate_api.api.collateral_loan_api import CollateralLoanApi
from gate_api.api.delivery_api import DeliveryApi
from gate_api.api.earn_api import EarnApi
from gate_api.api.flash_swap_api import FlashSwapApi
from gate_api.api.futures_api import FuturesApi
from gate_api.api.margin_api import MarginApi
from gate_api.api.multi_collateral_loan_api import MultiCollateralLoanApi
from gate_api.api.options_api import OptionsApi
from gate_api.api.rebate_api import RebateApi
from gate_api.api.spot_api import SpotApi
from gate_api.api.wallet_api import WalletApi
from gate_api.api.withdrawal_api import WithdrawalApi

# import ApiClient
from gate_api.api_client import ApiClient
from gate_api.configuration import Configuration
from gate_api.exceptions import OpenApiException
from gate_api.exceptions import ApiTypeError
from gate_api.exceptions import ApiValueError
from gate_api.exceptions import ApiKeyError
from gate_api.exceptions import ApiException
# import models into sdk package
from gate_api.models.account_balance import AccountBalance
from gate_api.models.account_detail import AccountDetail
from gate_api.models.account_detail_key import AccountDetailKey
from gate_api.models.account_rate_limit import AccountRateLimit
from gate_api.models.agency_commission import AgencyCommission
from gate_api.models.agency_commission_history import AgencyCommissionHistory
from gate_api.models.agency_transaction import AgencyTransaction
from gate_api.models.agency_transaction_history import AgencyTransactionHistory
from gate_api.models.auto_repay_setting import AutoRepaySetting
from gate_api.models.batch_amend_item import BatchAmendItem
from gate_api.models.batch_amend_order_req import BatchAmendOrderReq
from gate_api.models.batch_futures_order import BatchFuturesOrder
from gate_api.models.batch_order import BatchOrder
from gate_api.models.borrow_currency_info import BorrowCurrencyInfo
from gate_api.models.broker_commission import BrokerCommission
from gate_api.models.broker_commission1 import BrokerCommission1
from gate_api.models.broker_transaction import BrokerTransaction
from gate_api.models.broker_transaction1 import BrokerTransaction1
from gate_api.models.cancel_batch_order import CancelBatchOrder
from gate_api.models.cancel_order_result import CancelOrderResult
from gate_api.models.collateral_adjust import CollateralAdjust
from gate_api.models.collateral_adjust_res import CollateralAdjustRes
from gate_api.models.collateral_align import CollateralAlign
from gate_api.models.collateral_currency import CollateralCurrency
from gate_api.models.collateral_currency_info import CollateralCurrencyInfo
from gate_api.models.collateral_currency_res import CollateralCurrencyRes
from gate_api.models.collateral_current_rate import CollateralCurrentRate
from gate_api.models.collateral_fix_rate import CollateralFixRate
from gate_api.models.collateral_loan_currency import CollateralLoanCurrency
from gate_api.models.collateral_ltv import CollateralLtv
from gate_api.models.collateral_order import CollateralOrder
from gate_api.models.collateral_record import CollateralRecord
from gate_api.models.contract import Contract
from gate_api.models.contract_stat import ContractStat
from gate_api.models.convert_small_balance import ConvertSmallBalance
from gate_api.models.countdown_cancel_all_futures_task import CountdownCancelAllFuturesTask
from gate_api.models.countdown_cancel_all_options_task import CountdownCancelAllOptionsTask
from gate_api.models.countdown_cancel_all_spot_task import CountdownCancelAllSpotTask
from gate_api.models.create_collateral_order import CreateCollateralOrder
from gate_api.models.create_multi_collateral_order import CreateMultiCollateralOrder
from gate_api.models.create_uni_lend import CreateUniLend
from gate_api.models.create_uni_loan import CreateUniLoan
from gate_api.models.cross_margin_account import CrossMarginAccount
from gate_api.models.cross_margin_account_book import CrossMarginAccountBook
from gate_api.models.cross_margin_balance import CrossMarginBalance
from gate_api.models.cross_margin_balance1 import CrossMarginBalance1
from gate_api.models.cross_margin_currency import CrossMarginCurrency
from gate_api.models.cross_margin_loan import CrossMarginLoan
from gate_api.models.cross_margin_repay_request import CrossMarginRepayRequest
from gate_api.models.cross_margin_repayment import CrossMarginRepayment
from gate_api.models.cross_margin_transferable import CrossMarginTransferable
from gate_api.models.currency import Currency
from gate_api.models.currency_chain import CurrencyChain
from gate_api.models.currency_pair import CurrencyPair
from gate_api.models.currency_quota import CurrencyQuota
from gate_api.models.delivery_candlestick import DeliveryCandlestick
from gate_api.models.delivery_contract import DeliveryContract
from gate_api.models.delivery_settlement import DeliverySettlement
from gate_api.models.deposit_address import DepositAddress
from gate_api.models.dual_get_orders import DualGetOrders
from gate_api.models.dual_get_plans import DualGetPlans
from gate_api.models.eth2_swap import Eth2Swap
from gate_api.models.flash_swap_currency import FlashSwapCurrency
from gate_api.models.flash_swap_currency_pair import FlashSwapCurrencyPair
from gate_api.models.flash_swap_order import FlashSwapOrder
from gate_api.models.flash_swap_order_preview import FlashSwapOrderPreview
from gate_api.models.flash_swap_order_request import FlashSwapOrderRequest
from gate_api.models.flash_swap_preview_request import FlashSwapPreviewRequest
from gate_api.models.funding_account import FundingAccount
from gate_api.models.funding_book_item import FundingBookItem
from gate_api.models.funding_rate_record import FundingRateRecord
from gate_api.models.future_cancel_order_result import FutureCancelOrderResult
from gate_api.models.futures_account import FuturesAccount
from gate_api.models.futures_account_book import FuturesAccountBook
from gate_api.models.futures_account_history import FuturesAccountHistory
from gate_api.models.futures_auto_deleverage import FuturesAutoDeleverage
from gate_api.models.futures_batch_amend_order_request import FuturesBatchAmendOrderRequest
from gate_api.models.futures_candlestick import FuturesCandlestick
from gate_api.models.futures_fee import FuturesFee
from gate_api.models.futures_index_constituents import FuturesIndexConstituents
from gate_api.models.futures_initial_order import FuturesInitialOrder
from gate_api.models.futures_limit_risk_tiers import FuturesLimitRiskTiers
from gate_api.models.futures_liq_order import FuturesLiqOrder
from gate_api.models.futures_liquidate import FuturesLiquidate
from gate_api.models.futures_order import FuturesOrder
from gate_api.models.futures_order_amendment import FuturesOrderAmendment
from gate_api.models.futures_order_book import FuturesOrderBook
from gate_api.models.futures_order_book_item import FuturesOrderBookItem
from gate_api.models.futures_premium_index import FuturesPremiumIndex
from gate_api.models.futures_price_trigger import FuturesPriceTrigger
from gate_api.models.futures_price_triggered_order import FuturesPriceTriggeredOrder
from gate_api.models.futures_ticker import FuturesTicker
from gate_api.models.futures_trade import FuturesTrade
from gate_api.models.index_constituent import IndexConstituent
from gate_api.models.inline_object import InlineObject
from gate_api.models.inline_response200 import InlineResponse200
from gate_api.models.inline_response2001 import InlineResponse2001
from gate_api.models.insurance_record import InsuranceRecord
from gate_api.models.ledger_record import LedgerRecord
from gate_api.models.liquidate_order import LiquidateOrder
from gate_api.models.loan import Loan
from gate_api.models.loan_patch import LoanPatch
from gate_api.models.loan_record import LoanRecord
from gate_api.models.margin_account import MarginAccount
from gate_api.models.margin_account_book import MarginAccountBook
from gate_api.models.margin_account_currency import MarginAccountCurrency
from gate_api.models.margin_borrowable import MarginBorrowable
from gate_api.models.margin_currency_pair import MarginCurrencyPair
from gate_api.models.margin_tiers import MarginTiers
from gate_api.models.margin_transferable import MarginTransferable
from gate_api.models.max_uni_borrowable import MaxUniBorrowable
from gate_api.models.mock_futures_order import MockFuturesOrder
from gate_api.models.mock_futures_position import MockFuturesPosition
from gate_api.models.mock_margin_result import MockMarginResult
from gate_api.models.mock_options_order import MockOptionsOrder
from gate_api.models.mock_options_position import MockOptionsPosition
from gate_api.models.mock_risk_unit import MockRiskUnit
from gate_api.models.mock_spot_balance import MockSpotBalance
from gate_api.models.mock_spot_order import MockSpotOrder
from gate_api.models.multi_chain_address_item import MultiChainAddressItem
from gate_api.models.multi_collateral_currency import MultiCollateralCurrency
from gate_api.models.multi_collateral_item import MultiCollateralItem
from gate_api.models.multi_collateral_order import MultiCollateralOrder
from gate_api.models.multi_collateral_record import MultiCollateralRecord
from gate_api.models.multi_collateral_record_currency import MultiCollateralRecordCurrency
from gate_api.models.multi_loan_item import MultiLoanItem
from gate_api.models.multi_loan_repay_item import MultiLoanRepayItem
from gate_api.models.multi_repay_record import MultiRepayRecord
from gate_api.models.multi_repay_resp import MultiRepayResp
from gate_api.models.my_futures_trade import MyFuturesTrade
from gate_api.models.my_futures_trade_time_range import MyFuturesTradeTimeRange
from gate_api.models.open_orders import OpenOrders
from gate_api.models.options_account import OptionsAccount
from gate_api.models.options_account_book import OptionsAccountBook
from gate_api.models.options_candlestick import OptionsCandlestick
from gate_api.models.options_contract import OptionsContract
from gate_api.models.options_mmp import OptionsMMP
from gate_api.models.options_mmp_reset import OptionsMMPReset
from gate_api.models.options_my_settlements import OptionsMySettlements
from gate_api.models.options_my_trade import OptionsMyTrade
from gate_api.models.options_order import OptionsOrder
from gate_api.models.options_position import OptionsPosition
from gate_api.models.options_position_close import OptionsPositionClose
from gate_api.models.options_position_close_order import OptionsPositionCloseOrder
from gate_api.models.options_settlement import OptionsSettlement
from gate_api.models.options_ticker import OptionsTicker
from gate_api.models.options_underlying import OptionsUnderlying
from gate_api.models.options_underlying_ticker import OptionsUnderlyingTicker
from gate_api.models.order import Order
from gate_api.models.order_book import OrderBook
from gate_api.models.order_cancel import OrderCancel
from gate_api.models.order_patch import OrderPatch
from gate_api.models.order_resp import OrderResp
from gate_api.models.partner_commission_history import PartnerCommissionHistory
from gate_api.models.partner_sub import PartnerSub
from gate_api.models.partner_sub_list import PartnerSubList
from gate_api.models.partner_transaction_history import PartnerTransactionHistory
from gate_api.models.patch_uni_lend import PatchUniLend
from gate_api.models.place_dual_investment_order import PlaceDualInvestmentOrder
from gate_api.models.position import Position
from gate_api.models.position_close import PositionClose
from gate_api.models.position_close_order import PositionCloseOrder
from gate_api.models.profit_loss_range import ProfitLossRange
from gate_api.models.rebate_user_info import RebateUserInfo
from gate_api.models.repay_currency_res import RepayCurrencyRes
from gate_api.models.repay_loan import RepayLoan
from gate_api.models.repay_multi_loan import RepayMultiLoan
from gate_api.models.repay_record import RepayRecord
from gate_api.models.repay_record_currency import RepayRecordCurrency
from gate_api.models.repay_record_left_interest import RepayRecordLeftInterest
from gate_api.models.repay_record_repaid_currency import RepayRecordRepaidCurrency
from gate_api.models.repay_record_total_interest import RepayRecordTotalInterest
from gate_api.models.repay_request import RepayRequest
from gate_api.models.repay_resp import RepayResp
from gate_api.models.repayment import Repayment
from gate_api.models.risk_units import RiskUnits
from gate_api.models.saved_address import SavedAddress
from gate_api.models.small_balance import SmallBalance
from gate_api.models.small_balance_history import SmallBalanceHistory
from gate_api.models.spot_account import SpotAccount
from gate_api.models.spot_account_book import SpotAccountBook
from gate_api.models.spot_fee import SpotFee
from gate_api.models.spot_price_put_order import SpotPricePutOrder
from gate_api.models.spot_price_trigger import SpotPriceTrigger
from gate_api.models.spot_price_triggered_order import SpotPriceTriggeredOrder
from gate_api.models.stp_group import StpGroup
from gate_api.models.stp_group_user import StpGroupUser
from gate_api.models.structured_buy import StructuredBuy
from gate_api.models.structured_get_project_list import StructuredGetProjectList
from gate_api.models.structured_order_list import StructuredOrderList
from gate_api.models.sub_account import SubAccount
from gate_api.models.sub_account_balance import SubAccountBalance
from gate_api.models.sub_account_cross_margin_balance import SubAccountCrossMarginBalance
from gate_api.models.sub_account_futures_balance import SubAccountFuturesBalance
from gate_api.models.sub_account_key import SubAccountKey
from gate_api.models.sub_account_key_perms import SubAccountKeyPerms
from gate_api.models.sub_account_margin_balance import SubAccountMarginBalance
from gate_api.models.sub_account_to_sub_account import SubAccountToSubAccount
from gate_api.models.sub_account_transfer import SubAccountTransfer
from gate_api.models.sub_cross_margin_account import SubCrossMarginAccount
from gate_api.models.sub_user_mode import SubUserMode
from gate_api.models.system_time import SystemTime
from gate_api.models.ticker import Ticker
from gate_api.models.total_balance import TotalBalance
from gate_api.models.trade import Trade
from gate_api.models.trade_fee import TradeFee
from gate_api.models.transaction_id import TransactionID
from gate_api.models.transfer import Transfer
from gate_api.models.trigger_order_response import TriggerOrderResponse
from gate_api.models.trigger_time import TriggerTime
from gate_api.models.uid_push_order import UidPushOrder
from gate_api.models.uid_push_withdrawal import UidPushWithdrawal
from gate_api.models.uid_push_withdrawal_resp import UidPushWithdrawalResp
from gate_api.models.uni_currency import UniCurrency
from gate_api.models.uni_currency_interest import UniCurrencyInterest
from gate_api.models.uni_currency_pair import UniCurrencyPair
from gate_api.models.uni_interest_mode import UniInterestMode
from gate_api.models.uni_interest_record import UniInterestRecord
from gate_api.models.uni_lend import UniLend
from gate_api.models.uni_lend_interest import UniLendInterest
from gate_api.models.uni_lend_record import UniLendRecord
from gate_api.models.uni_loan import UniLoan
from gate_api.models.uni_loan_interest_record import UniLoanInterestRecord
from gate_api.models.uni_loan_record import UniLoanRecord
from gate_api.models.unified_account import UnifiedAccount
from gate_api.models.unified_balance import UnifiedBalance
from gate_api.models.unified_borrowable import UnifiedBorrowable
from gate_api.models.unified_discount import UnifiedDiscount
from gate_api.models.unified_discount_tiers import UnifiedDiscountTiers
from gate_api.models.unified_leverage_config import UnifiedLeverageConfig
from gate_api.models.unified_leverage_setting import UnifiedLeverageSetting
from gate_api.models.unified_loan import UnifiedLoan
from gate_api.models.unified_loan_record import UnifiedLoanRecord
from gate_api.models.unified_margin_tiers import UnifiedMarginTiers
from gate_api.models.unified_mode import UnifiedMode
from gate_api.models.unified_mode_set import UnifiedModeSet
from gate_api.models.unified_portfolio_input import UnifiedPortfolioInput
from gate_api.models.unified_portfolio_output import UnifiedPortfolioOutput
from gate_api.models.unified_risk_units import UnifiedRiskUnits
from gate_api.models.unified_settings import UnifiedSettings
from gate_api.models.unified_transferable import UnifiedTransferable
from gate_api.models.user_ltv_info import UserLtvInfo
from gate_api.models.user_total_amount import UserTotalAmount
from gate_api.models.withdraw_status import WithdrawStatus
from gate_api.models.withdrawal_record import WithdrawalRecord

