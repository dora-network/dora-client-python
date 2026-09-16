# Web3WithdrawalStatus

Lifecycle state of a web3 USDC withdrawal.  A withdrawal is created as `PENDING` with its quantity reserved against the account's available balance. Requesting a withdrawal is free, so no fee is reserved at that point and `fee` is 0. The reservation is consumed at `CONFIRMED` and released back to available at `REJECTED` or `FAILED`.  The usual path is `PENDING` -> `APPROVED_WITHOUT_FEE` -> `APPROVED` -> `BROADCAST` -> `SUBMITTED` -> `CONFIRMED`. `REJECTED` is reachable from `PENDING` and `APPROVED_WITHOUT_FEE`, the two states no fee has been locked against; `FAILED` only after a fee is locked. `CONFIRMED`, `REJECTED`, and `FAILED` are terminal.  - `PENDING`: awaiting admin review. The quantity is reserved but not yet spent, and no fee has been quoted. - `APPROVED_WITHOUT_FEE`: an admin approved the request, but its fee has not been quoted or locked yet, so it is not queued for on-chain submission. Every admin approval lands here. Locking the quoted fee reserves it on top of the quantity and moves the withdrawal to `APPROVED`; until then the approval is still reversible and the withdrawal may be rejected. - `APPROVED`: approved and fee-locked; it is queued for on-chain submission. - `BROADCAST`: the on-chain withdraw() transaction has been signed and sent, and `tx_hash` is set. The transaction is in the mempool and has not yet been seen in a block. - `SUBMITTED`: the transaction has been observed in a block and the funds have left the vault. Not yet final: if that block is reorganized out, the withdrawal returns to `BROADCAST` to be observed again. - `CONFIRMED`: the on-chain withdrawal finalized and the reservation was settled into an external debit (`settlement_transaction_id` is set). - `REJECTED`: an admin rejected the request while it was `PENDING` or `APPROVED_WITHOUT_FEE`. Nothing was sent on-chain and the reservation has been returned to the available balance. A withdrawal rejected after approval keeps its `approved_by`/`approved_at`. - `FAILED`: the withdrawal could not be executed after approval. The reservation has been returned to the available balance.

## Enum

* `PENDING` (value: `'PENDING'`)

* `APPROVED_WITHOUT_FEE` (value: `'APPROVED_WITHOUT_FEE'`)

* `APPROVED` (value: `'APPROVED'`)

* `BROADCAST` (value: `'BROADCAST'`)

* `SUBMITTED` (value: `'SUBMITTED'`)

* `CONFIRMED` (value: `'CONFIRMED'`)

* `REJECTED` (value: `'REJECTED'`)

* `FAILED` (value: `'FAILED'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


