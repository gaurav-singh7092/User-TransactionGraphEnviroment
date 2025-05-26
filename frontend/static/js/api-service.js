/**
 * API Service for interacting with the backend
 */
class ApiService {
    constructor(config) {
        this.config = config;
    }

    /**
     * Fetch all users from the API
     * @returns {Promise<Array>} Array of user objects
     */
    async getUsers() {
        try {
            const response = await fetch(`${this.config.BASE_URL}${this.config.USERS}`);
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching users:', error);
            throw error;
        }
    }

    /**
     * Fetch all transactions from the API
     * @returns {Promise<Array>} Array of transaction objects
     */
    async getTransactions() {
        try {
            const response = await fetch(`${this.config.BASE_URL}${this.config.TRANSACTIONS}`);
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching transactions:', error);
            throw error;
        }
    }

    /**
     * Fetch relationships for a specific user
     * @param {string} userId - The ID of the user
     * @returns {Promise<Object>} User relationship data
     */
    async getUserRelationships(userId) {
        try {
            const response = await fetch(`${this.config.BASE_URL}${this.config.USER_RELATIONSHIPS}${userId}`);
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`Error fetching relationships for user ${userId}:`, error);
            throw error;
        }
    }

    /**
     * Fetch business relationships for a specific user
     * @param {string} userId - The ID of the user
     * @returns {Promise<Object>} Business relationship data
     */
    async getBusinessRelationships(userId) {
        try {
            const response = await fetch(`${this.config.BASE_URL}${this.config.BUSINESS_RELATIONSHIPS}${userId}`);
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`Error fetching business relationships for user ${userId}:`, error);
            throw error;
        }
    }

    /**
     * Fetch relationships for a specific transaction
     * @param {string} transactionId - The ID of the transaction
     * @returns {Promise<Object>} Transaction relationship data
     */
    async getTransactionRelationships(transactionId) {
        try {
            const response = await fetch(`${this.config.BASE_URL}${this.config.TRANSACTION_RELATIONSHIPS}${transactionId}`);
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`Error fetching relationships for transaction ${transactionId}:`, error);
            throw error;
        }
    }

    /**
     * Trigger relationship detection on the server
     * @returns {Promise<Object>} Response from the server
     */
    async detectRelationships() {
        try {
            const response = await fetch(`${this.config.BASE_URL}${this.config.DETECT_RELATIONSHIPS}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error detecting relationships:', error);
            throw error;
        }
    }
}

// Create an instance of the API service
const apiService = new ApiService(CONFIG.API);
