from .common import router, ln, BaseClient
from .errors import handle_rpc_errors
from datetime import datetime
import binascii

class RouterRPC(BaseClient):

    # ROUTERRPC
    @handle_rpc_errors
    def build_route(self, amt_msat, oid, hop_pubkeys, **kwargs):
        hop_pubkeys_bytes = [ bytes.fromhex(pk) for pk in hop_pubkeys ]
        hop_pubkeys_check = [ pk.hex() for pk in hop_pubkeys_bytes ]
        #print(hop_pubkeys_bytes)
        #print("\n".join(map(str, hop_pubkeys_check)))

        request = router.BuildRouteRequest(
            amt_msat=amt_msat,
            outgoing_chan_id=oid,
            hop_pubkeys=hop_pubkeys_bytes,
            final_cltv_delta=400,
            **kwargs
        )
        try:
            response = self._router_stub.BuildRoute(request)
        except Exception as error:
            print(error)
            raise error

        return response

    @handle_rpc_errors
    def send_to_route(self, pay_hash, route):
        request = router.SendToRouteRequest(
            payment_hash=pay_hash,
            route=route,
        )

        response = self._router_stub.SendToRouteV2(request)
        return response

    @handle_rpc_errors
    def send_payment_v2(self, **kwargs):
        request = router.SendPaymentRequest(**kwargs)
        for response in self._router_stub.SendPaymentV2(request):
            yield response

    @handle_rpc_errors
    def send_payment_v1(self, **kwargs):
        request = router.SendPaymentRequest(**kwargs)
        response = self._router_stub.SendPayment(request)
        return response

    @handle_rpc_errors
    def reset_mission_control(self):
        request = router.ResetMissionControlRequest()
        response = self._router_stub.ResetMissionControl(request)
        return response

    @handle_rpc_errors
    def update_chan_status(self, chan_point, action):
        """
        Router.UpdateChanStatus
        Update
        ENABLE 0
        DISABLE 1
        AUTO 2
        """
        funding_txid_str, output_index = chan_point.split(":")
        output_index = int(output_index)
        channel_point = ln.ChannelPoint(funding_txid_str=funding_txid_str, output_index=output_index)

        request = router.UpdateChanStatusRequest(
            chan_point=channel_point,
            action=action
        )
        response = self._router_stub.UpdateChanStatus(request)
        return response

    @handle_rpc_errors
    def track_payment_v2(self, payment_hash, no_inflight_updates=False):
        """Subscribe to the state of a single outbound payment"""
        request = router.TrackPaymentRequest(payment_hash=bytes.fromhex(payment_hash), no_inflight_updates=no_inflight_updates)
        for response in self._router_stub.TrackPaymentV2(request):
            yield response

    @handle_rpc_errors
    def track_payments(self, no_inflight_updates=False):
        """Subscribe to the state of all outbound payments"""
        request = router.TrackPaymentsRequest(no_inflight_updates=no_inflight_updates)
        for response in self._router_stub.TrackPayments(request):
            yield response

